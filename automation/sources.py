"""
Paper sources: the daily arXiv crawl and the owner's inbox issue.

All arXiv and network logic lives in this module; the pipeline and the (temporary)
migration tooling import from here. Functions produce ready `Paper` objects:
metadata from the arXiv Atom API, venue "arXiv YYYY/MM" derived from the v1 date,
and abstracts cached into the sidecar (data/abstracts.json) so classification and
later passes never refetch.
"""

from __future__ import annotations

import json
import logging
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from functools import lru_cache

from automation import config, storage
from automation.models import Paper

logger = logging.getLogger(__name__)

ARXIV_ID = re.compile(r"^\d{4}\.\d{4,5}$")
_ATOM = {"a": "http://www.w3.org/2005/Atom"}
_API = "https://export.arxiv.org/api/query"
_SLEEP_S = 3  # arXiv rate courtesy between requests


# ── Venue extraction ──────────────────────────────────────────────────────────
# Authors often state acceptance in the abstract ("Accepted at ICSE 2026").
# Ported from the old enricher; the owner can always fix a venue during review
# with `/edit N venue=...`.

_VENUE_ACCEPT_RE = re.compile(
    r"(?:accepted (?:at|to|in|by)|to appear (?:at|in)|published (?:at|in)|presented at)\s+"
    r"((?:the\s+)?[\w\s\-+/&]+?\d{4})",
    re.IGNORECASE,
)
_VENUE_NAME_RE = re.compile(
    r"\b((?:ICSE|FSE|ASE|ISSTA|PLDI|POPL|OOPSLA|SOSP|OSDI|ASPLOS|MICRO|ISCA"
    r"|NeurIPS|ICML|ICLR|ACL|EMNLP|NAACL|COLM|CVPR|ICCV|ECCV|AAAI|IJCAI"
    r"|CCS|USENIX Security|Oakland|NDSS|CHI|CSCW|VLDB|SIGMOD|ICDE|KDD|WWW"
    r"|MSR|ICST|SANER|ICSME|TOSEM|TSE|EMSE)\s*'?\d{2,4})\b"
)


def extract_venue(abstract: str, default: str) -> str:
    """Venue from acceptance phrases in the abstract; falls back to the default."""
    for rx in (_VENUE_ACCEPT_RE, _VENUE_NAME_RE):
        m = rx.search(abstract)
        if m:
            venue = re.sub(r"\s+", " ", m.group(1)).strip(" .,")
            venue = re.sub(r"^the\s+", "", venue, flags=re.IGNORECASE)
            if len(venue) <= 40:  # long captures are almost always false positives
                return venue
    return default


# ── Atom feed parsing ─────────────────────────────────────────────────────────

def _feed_entries(xml_bytes: bytes) -> list[tuple[Paper, str]]:
    """Parse an arXiv Atom feed into (Paper, abstract) pairs."""
    out: list[tuple[Paper, str]] = []
    root = ET.fromstring(xml_bytes)
    for entry in root.findall("a:entry", _ATOM):
        eid = entry.find("a:id", _ATOM)
        m = re.search(r"abs/(\d{4}\.\d{4,5})", eid.text or "") if eid is not None else None
        if not m:
            continue
        pid = m.group(1)
        title = re.sub(r"\s+", " ", entry.find("a:title", _ATOM).text or "").strip()
        authors = [a.find("a:name", _ATOM).text or "" for a in entry.findall("a:author", _ATOM)]
        pub = entry.find("a:published", _ATOM)
        published = (pub.text or "")[:10] if pub is not None else ""
        summary = entry.find("a:summary", _ATOM)
        abstract = re.sub(r"\s+", " ", summary.text or "").strip() if summary is not None else ""
        default = f"arXiv {published[:4]}/{published[5:7]}" if published else "arXiv"
        venue = extract_venue(abstract, default)
        paper = Paper(
            id=pid, title=title, authors=authors, venue=venue, published=published,
            links={"paper": f"https://arxiv.org/abs/{pid}"},
        )
        out.append((paper, abstract))
    return out


def _query(params: dict[str, str]) -> list[tuple[Paper, str]]:
    url = _API + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url, timeout=60) as r:
        return _feed_entries(r.read())


def _cache_abstracts(pairs: list[tuple[Paper, str]]) -> None:
    cache = storage.load_abstracts()
    changed = False
    for paper, abstract in pairs:
        if abstract and paper.id not in cache:
            cache[paper.id] = abstract
            changed = True
    if changed:
        storage.save_abstracts(cache)


# ── arXiv metadata by id ──────────────────────────────────────────────────────

def fetch_arxiv_papers(ids: list[str]) -> dict[str, Paper]:
    """Build Paper objects from the arXiv API; abstracts go into the sidecar."""
    out: dict[str, Paper] = {}
    arxiv_ids = [i for i in ids if ARXIV_ID.match(i)]
    for start in range(0, len(arxiv_ids), 50):
        chunk = arxiv_ids[start:start + 50]
        logger.info("fetching metadata for %d papers from arXiv", len(chunk))
        pairs = _query({"max_results": "100", "id_list": ",".join(chunk)})
        _cache_abstracts(pairs)
        for paper, _ in pairs:
            out[paper.id] = paper
        time.sleep(_SLEEP_S)
    return out


def ensure_abstracts(ids: list[str]) -> dict[str, str]:
    """Return the abstract sidecar with the given arXiv ids fetched if missing."""
    cache = storage.load_abstracts()
    missing = [i for i in ids if ARXIV_ID.match(i) and i not in cache]
    if missing:
        fetch_arxiv_papers(missing)  # caches abstracts as a side effect
        cache = storage.load_abstracts()
    return cache


def fetch_published(ids: list[str]) -> dict[str, str]:
    """id -> first-publication date (arXiv v1), YYYY-MM-DD."""
    return {pid: p.published for pid, p in fetch_arxiv_papers(ids).items() if p.published}


# ── Abstract recovery for non-arXiv papers ────────────────────────────────────

def _norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", t.lower())


def search_arxiv_by_title(title: str) -> str | None:
    """Find a paper's arXiv abstract by exact-ish title match; None if absent."""
    try:
        pairs = _query({"search_query": f'ti:"{title}"', "max_results": "5"})
    except Exception as exc:
        logger.warning("arxiv title search failed for %r: %s", title[:50], exc)
        return None
    want = _norm_title(title)
    for paper, abstract in pairs:
        got = _norm_title(paper.title)
        if got == want or got.startswith(want) or want.startswith(got):
            return abstract or None
    return None


def fetch_landing_abstract(url: str) -> str | None:
    """Best-effort abstract extraction from a paper's landing page (meta tags, ACL div)."""
    if not url.startswith("http"):
        return None
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (paper-metadata-fetch)"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", errors="replace")
    except Exception as exc:
        logger.warning("landing fetch failed for %s: %s", url[:60], exc)
        return None
    for pattern in (
        r'name="citation_abstract"\s+content="([^"]{100,})"',
        r'property="og:description"\s+content="([^"]{100,})"',
        r'class="[^"]*acl-abstract[^"]*"[^>]*>\s*(?:<[^>]+>)*([^<]{100,})',
    ):
        m = re.search(pattern, html, re.DOTALL)
        if m:
            import html as _html
            return re.sub(r"\s+", " ", _html.unescape(m.group(1))).strip()
    return None


def ensure_primary_abstracts(papers: list[Paper]) -> dict[str, str]:
    """Primary-source abstracts for any papers: arXiv id -> arXiv title search ->
    landing page. Results cached in the sidecar under each paper's id."""
    cache = ensure_abstracts([p.id for p in papers])
    changed = False
    for p in papers:
        if p.id in cache or ARXIV_ID.match(p.id):
            continue
        ab = search_arxiv_by_title(p.title)
        time.sleep(_SLEEP_S)
        if not ab:
            ab = fetch_landing_abstract(p.links.get("paper", ""))
        if ab:
            cache[p.id] = ab
            changed = True
            logger.info("recovered abstract for: %s", p.title[:60])
        else:
            logger.info("no primary abstract found: %s", p.title[:60])
    if changed:
        storage.save_abstracts(cache)
    return cache


# ── Keyword pre-filter ────────────────────────────────────────────────────────

@lru_cache(maxsize=4)
def _keyword_regex(keywords: tuple[str, ...]) -> re.Pattern:
    alts = "|".join(re.escape(k.lower()) for k in keywords)
    return re.compile(r"\b(?:" + alts + r")\b")


def keyword_hit(text: str, keywords: list[str]) -> bool:
    """Case-insensitive whole-word/phrase match of any keyword in the text."""
    return bool(_keyword_regex(tuple(keywords)).search(text.lower()))


# ── The two sources ───────────────────────────────────────────────────────────
# The daily source is arXiv's OAI-PMH interface, which is indexed by ANNOUNCEMENT
# date (exactly the "last night's mailing" semantics). The search API only filters
# by submission date, which lags announcements by up to four days over weekends.

_OAI = {
    "oai": "http://www.openarchives.org/OAI/2.0/",
    "ax": "http://arxiv.org/OAI/arXiv/",
}
_OAI_BASE = "https://export.arxiv.org/oai2"


def _oai_page(url: str) -> tuple[list[tuple[Paper, str, set[str]]], str]:
    """One OAI-PMH page, honoring arXiv's 503 Retry-After flow control."""
    for attempt in range(3):
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (paper-metadata-fetch)"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            break
        except urllib.error.HTTPError as exc:
            if exc.code == 503 and attempt < 2:
                wait = int(exc.headers.get("Retry-After", "10") or "10")
                logger.info("OAI 503, retrying in %ds", wait)
                time.sleep(wait)
                continue
            raise
    return _oai_parse(data)


def _oai_parse(data: bytes) -> tuple[list[tuple[Paper, str, set[str], str]], str]:
    """Parse an OAI-PMH page into ((paper, abstract, categories, announced) quads,
    resumption token). `announced` is the record's datestamp (announcement day)."""
    root = ET.fromstring(data)
    out: list[tuple[Paper, str, set[str], str]] = []
    for rec in root.findall(".//oai:record", _OAI):
        announced = (rec.findtext("oai:header/oai:datestamp", "", _OAI) or "")[:10]
        meta = rec.find(".//ax:arXiv", _OAI)
        if meta is None:  # deleted records carry no metadata
            continue
        pid = (meta.findtext("ax:id", "", _OAI) or "").strip()
        title = re.sub(r"\s+", " ", meta.findtext("ax:title", "", _OAI) or "").strip()
        abstract = re.sub(r"\s+", " ", meta.findtext("ax:abstract", "", _OAI) or "").strip()
        created = (meta.findtext("ax:created", "", _OAI) or "").strip()  # v1 date
        cats = set((meta.findtext("ax:categories", "", _OAI) or "").split())
        authors = []
        for a in meta.findall("ax:authors/ax:author", _OAI):
            fore = (a.findtext("ax:forenames", "", _OAI) or "").strip()
            key = (a.findtext("ax:keyname", "", _OAI) or "").strip()
            authors.append(f"{fore} {key}".strip())
        default = f"arXiv {created[:4]}/{created[5:7]}" if created else "arXiv"
        paper = Paper(
            id=pid, title=title, authors=authors,
            venue=extract_venue(abstract, default), published=created,
            links={"paper": f"https://arxiv.org/abs/{pid}"},
        )
        out.append((paper, abstract, cats, announced))
    token = (root.findtext(".//oai:resumptionToken", "", _OAI) or "").strip()
    return out, token


def harvest_announced(since: str, until: str | None = None) -> tuple[list[Paper], dict[str, int]]:
    """Keyword-matching papers ANNOUNCED (or updated) in [since, until] (YYYY-MM-DD,
    inclusive; until defaults to today). The single source for both the daily crawl
    and historical backfill. Returns (candidates, per-day scanned-record counts);
    the counts cover every day in the range (0 for quiet days), forming the ledger
    entry that proves the day was swept."""
    from datetime import date, timedelta

    cfg = config.load()["arxiv"]
    wanted = set(cfg["categories"])
    keywords = cfg["keywords"]
    url = f"{_OAI_BASE}?verb=ListRecords&metadataPrefix=arXiv&set=cs&from={since}"
    if until:
        url += f"&until={until}"
    found: dict[str, tuple[Paper, str]] = {}
    day_counts: dict[str, int] = {}
    # Pre-mark the whole requested range so quiet days are recorded as swept.
    d, end = date.fromisoformat(since), date.fromisoformat(until or str(date.today()))
    while d <= end:
        day_counts[str(d)] = 0
        d += timedelta(days=1)
    while url:
        records, token = _oai_page(url)
        for paper, abstract, cats, announced in records:
            if announced:
                day_counts[announced] = day_counts.get(announced, 0) + 1
            if not ARXIV_ID.match(paper.id):
                continue  # old-style ids predate our scope
            if not (cats & wanted):
                continue
            if not keyword_hit(paper.title + " " + abstract, keywords):
                continue
            found.setdefault(paper.id, (paper, abstract))
        url = (f"{_OAI_BASE}?verb=ListRecords&resumptionToken={urllib.parse.quote(token)}"
               if token else "")
        time.sleep(_SLEEP_S)
    logger.info("harvest %s..%s: %d announced records scanned, %d keyword hits",
                since, until or "today", sum(day_counts.values()), len(found))
    _cache_abstracts(list(found.values()))
    return [p for p, _ in found.values()], day_counts


_INBOX_LINK_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.IGNORECASE)


def _inbox_comments() -> list[dict]:
    cfg = config.load()
    owner, repo = cfg["repo"]["owner"], cfg["repo"]["name"]
    issue = cfg["inbox"]["issue_number"]
    raw = subprocess.run(
        ["gh", "api", "--paginate", f"repos/{owner}/{repo}/issues/{issue}/comments"],
        capture_output=True, text=True, timeout=120,
    )
    if raw.returncode != 0:
        raise RuntimeError(f"gh api failed: {raw.stderr[:300]}")
    return json.loads(raw.stdout)


def read_inbox() -> list[Paper]:
    """All arXiv papers linked in the inbox issue's comments (candidates only;
    the pipeline filters against known ids)."""
    comments = _inbox_comments()
    ids: list[str] = []
    for c in comments:
        for m in _INBOX_LINK_RE.findall(c.get("body", "")):
            if m not in ids:
                ids.append(m)
    logger.info("inbox: %d unique arXiv ids across %d comments", len(ids), len(comments))
    return list(fetch_arxiv_papers(ids).values())


def ack_inbox(handled: set[str]) -> None:
    """React with a thumbs-up to inbox comments whose linked papers have all been
    handled (stored, proposed, or auto-skipped). The reaction is the owner-facing
    acknowledgement that a pasted link was picked up."""
    cfg = config.load()
    owner, repo = cfg["repo"]["owner"], cfg["repo"]["name"]
    acked = 0
    for c in _inbox_comments():
        ids = _INBOX_LINK_RE.findall(c.get("body", ""))
        if not ids or not all(i in handled for i in ids):
            continue
        if (c.get("reactions") or {}).get("+1", 0) > 0:
            continue  # already acknowledged
        proc = subprocess.run(
            ["gh", "api", "--method", "POST",
             f"repos/{owner}/{repo}/issues/comments/{c['id']}/reactions",
             "-f", "content=+1"],
            capture_output=True, text=True, timeout=60,
        )
        if proc.returncode == 0:
            acked += 1
    if acked:
        logger.info("inbox: acknowledged %d comments", acked)


# ── Link enrichment (approved papers only; cheap and best-effort) ─────────────

def enrich_links(paper: Paper) -> None:
    """Fill links.github from the Hugging Face papers API when available."""
    if paper.links.get("github") or not ARXIV_ID.match(paper.id):
        return
    try:
        req = urllib.request.Request(
            f"https://huggingface.co/api/papers/{paper.id}",
            headers={"User-Agent": "Mozilla/5.0 (paper-metadata-fetch)"},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            text = r.read().decode("utf-8", errors="replace")
        m = re.search(r"https://github\.com/[\w.\-]+/[\w.\-]+", text)
        if m:
            paper.links["github"] = m.group(0).rstrip(".")
            logger.info("enriched github link for %s", paper.id)
    except Exception:
        pass  # 404 is the common case; enrichment is strictly best-effort
