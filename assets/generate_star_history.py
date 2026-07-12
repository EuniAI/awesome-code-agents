#!/usr/bin/env python3
"""Generate a self-hosted Star History chart (assets/star-history.svg).

star-history.com now requires each viewer to supply their own GitHub token
(GitHub restricted stargazer data), so its embedded SVG is permanently broken in
a README. Instead we read our own repo's star timestamps with the repo token and
render a static SVG, committed to the repo and refreshed weekly by
.github/workflows/star-history.yml. No third-party dependency, nothing to break.

Run: python assets/generate_star_history.py   (needs `gh` authenticated, or
GH_TOKEN set, with read access to the repo's stargazers).
"""
from __future__ import annotations

import json
import math
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = "EuniAI/awesome-code-agents"
OUT = Path(__file__).resolve().parent / "star-history.svg"

# Canvas + margins.
W, H = 820, 400
PAD_L, PAD_R, PAD_T, PAD_B = 62, 28, 26, 46
# Mid gray reads on both light and dark GitHub themes; gold nods to the star.
AXIS, TEXT, LINE, FILL = "#8b949e", "#8b949e", "#e3b341", "rgba(227,179,65,0.16)"


def _stargazer_times() -> list[datetime]:
    """Ascending list of star timestamps, paginated across all stargazers."""
    out = subprocess.run(
        ["gh", "api", "--paginate",
         "-H", "Accept: application/vnd.github.star+json",
         f"/repos/{REPO}/stargazers?per_page=100", "--jq", ".[].starred_at"],
        capture_output=True, text=True, timeout=180, check=True,
    ).stdout
    times = [datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
             for s in out.split() if s]
    return sorted(times)


def _nice_axis(nmax: int) -> tuple[int, int]:
    """A rounded y-axis top and step giving ~5 ticks."""
    if nmax <= 5:
        return 5, 1
    raw = nmax / 5
    mag = 10 ** math.floor(math.log10(raw))
    step = next(m * mag for m in (1, 2, 2.5, 5, 10) if m * mag >= raw)
    step = int(step) or 1
    return step * math.ceil(nmax / step), step


def _svg(times: list[datetime]) -> str:
    now = datetime.now(timezone.utc)
    n = len(times)
    t0 = times[0] if times else now
    top, step = _nice_axis(max(n, 1))
    span = max((now - t0).total_seconds(), 1)
    plot_w, plot_h = W - PAD_L - PAD_R, H - PAD_T - PAD_B
    base = H - PAD_B

    def X(t: datetime) -> float:
        return PAD_L + (t - t0).total_seconds() / span * plot_w

    def Y(c: float) -> float:
        return base - c / top * plot_h

    # Cumulative curve: (first star, 0) -> each star -> flat to today.
    pts = [(X(t0), Y(0))]
    pts += [(X(t), Y(i)) for i, t in enumerate(times, start=1)]
    pts.append((X(now), Y(n)))
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area = f"{PAD_L:.1f},{base:.1f} " + line + f" {X(now):.1f},{base:.1f}"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" font-family="-apple-system,Segoe UI,sans-serif">',
        f'<text x="{PAD_L}" y="18" fill="{TEXT}" font-size="13" font-weight="600">'
        f'{REPO} &#8226; {n} stars</text>',
    ]
    # Horizontal gridlines + y labels.
    for c in range(0, top + 1, step):
        y = Y(c)
        parts.append(f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{W-PAD_R}" y2="{y:.1f}" '
                     f'stroke="{AXIS}" stroke-opacity="0.18" stroke-width="1"/>')
        parts.append(f'<text x="{PAD_L-8}" y="{y+4:.1f}" fill="{TEXT}" font-size="11" '
                     f'text-anchor="end">{c}</text>')
    # X date ticks (~5 across the range).
    for k in range(5):
        frac = k / 4
        t = datetime.fromtimestamp(t0.timestamp() + frac * span, tz=timezone.utc)
        x = PAD_L + frac * plot_w
        parts.append(f'<text x="{x:.1f}" y="{base+20:.1f}" fill="{TEXT}" font-size="11" '
                     f'text-anchor="middle">{t.strftime("%b %Y")}</text>')
    # Axes, area, curve.
    parts.append(f'<polygon points="{area}" fill="{FILL}" stroke="none"/>')
    parts.append(f'<polyline points="{line}" fill="none" stroke="{LINE}" '
                 f'stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>')
    parts.append(f'<line x1="{PAD_L}" y1="{PAD_T}" x2="{PAD_L}" y2="{base}" '
                 f'stroke="{AXIS}" stroke-width="1"/>')
    parts.append(f'<line x1="{PAD_L}" y1="{base}" x2="{W-PAD_R}" y2="{base}" '
                 f'stroke="{AXIS}" stroke-width="1"/>')
    parts.append(f'<circle cx="{X(now):.1f}" cy="{Y(n):.1f}" r="3.5" fill="{LINE}"/>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    times = _stargazer_times()
    OUT.write_text(_svg(times), encoding="utf-8")
    print(f"[OK] wrote {OUT} ({len(times)} stars)")


if __name__ == "__main__":
    main()
