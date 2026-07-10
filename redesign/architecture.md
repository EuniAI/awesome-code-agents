# Architecture (ground-up rebuild)

A clean rebuild of the automation pipeline and the data layer. The old pipeline is parked
in `_legacy/` and read only to recover edge-case knowledge (rate limits, dedup, inbox
reactions, venue parsing); its code is not copied. The new taxonomy lives in
`taxonomy.json`; this document is the blueprint for everything that consumes it.

## Principles

- Minimal and flat. No database, queue, plugin system, or async. Files + cron.
- One convention, one home: schema in `models`, data layout in `storage`, tree in
  `taxonomy`, README structure in `render`.
- Every stage is a pure function `list[Paper] -> list[Paper]`; IO at the edges; `main`
  only orchestrates.
- The pipeline can be down while we rebuild (cron is stopped). Nothing runs until we say.

## Data model

One record per paper, identified by its arXiv id.

```
Paper:
  id        str            # arxiv id, stable identity + dedup key
  title     str
  authors   list[str]
  venue     str
  published str            # first-publication date YYYY-MM-DD (drives the 6-month curation)
  links     {paper, github, website}
  category  str            # a taxonomy leaf key (the single classification field)
  tags      list[str]      # paper_type + released_artifact values
  summary   str            # 2-3 sentences, regenerated during the rebuild
```

Storage: one YAML file per taxonomy leaf, `data/papers_{leaf}.yaml`, newest first (fresh
folder, 23 files). `category` is carried in each record too, so re-classification is a
field change plus a save, never manual file surgery. Abstracts are raw source material,
not curated content: they live in a sidecar `data/abstracts.json` (id -> abstract),
fetched once and reused forever (re-classification when the taxonomy evolves, golden-set
evals, future search) instead of re-crawling arXiv each time. `storage` is the only
module that knows this layout.

## Modules (flat, under `automation/`)

Already built and kept: `taxonomy.py`, `render.py`, `tests/`.

```
models.py     Paper dataclass + (de)serialization. The one schema.
config.py     load operational config (repo, arxiv, llm, schedule). No categories/tags.
storage.py    the data/ layout: load/write/move/dedup by id. Sole owner of file names.
state.py      processed ids, retry counts (capped), dead-letter. Atomic writes.
sources.py    produce papers: arxiv crawl + inbox reader -> list[Paper].
enrich.py     fill venue and github/website links (arxiv + HF + GitHub search).
classify.py   Paper -> (category, tags, summary). Prompt compiled from taxonomy.json;
              structured output; runs on the Claude subscription (claude -p). Also the
              migration engine.
review.py     create per-batch GitHub review issues; poll /approve /reject /edit
              (category validated against taxonomy). github API calls live here.
render.py     README papers chapter + nav + summary count, from the tree. (built)
badges.py     papers-count endpoint json + acknowledgements section.
git.py        commit and push; calls render/badges as functions (no subprocess).
main.py       thin CLI: daily | finalize | render | migrate | setup.
```

## Data flow

```
daily:    sources -> enrich -> classify -> review(create issues)
finalize: review(poll approvals) -> storage.write -> render+badges -> git push
migrate:  read old data/*.yaml + rescue inbox -> classify (fresh) -> storage.write
```

## Build order

1. `models.py`, `config.py`, `storage.py` (new data model), adapt `render.py` to it.
2. `classify.py` (the migration engine) + a minimal `migrate` entry.
3. Re-classify all papers into the fresh `data/`: facts (title/authors/venue/links) kept
   from the old files and the inbox rescue set; category/tags/summary generated fresh.
   Human review per batch.
4. `sources.py`, `enrich.py`, `state.py`, `review.py`, `badges.py`, `git.py`, `main.py`.
5. Completeness diff against `_legacy/`; delete `_legacy/` and the old data files.
6. Resume cron.
```
