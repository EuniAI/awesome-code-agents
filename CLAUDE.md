# Awesome Code Agents — Project Context

## Working Preferences

- **Always work directly on `main`**, no worktrees. The owner wants changes visible immediately without manual merging.
- Commit and push after each logical change so nothing gets lost in a temporary branch.
- **Do NOT add `Co-Authored-By: Claude` to commit messages.** Commits should only show the owner's account.
- **This is an English-only repo.** Every file, including internal design docs, commit messages, and comments, must be written in English. No Chinese anywhere in the repo.
- **No em-dashes (—) in anything we write.** They read as AI-written. Use colons, commas, parentheses, or separate sentences instead. This applies to all repo files and commit messages. (Exception: never alter em-dashes inside a paper's own title or abstract, that is quoted source text.)

## What This Project Is

A curated list of research papers on autonomous code agents, maintained at [euni.ai](https://euni.ai).
Papers are stored as YAML files in `data/`, rendered into `README.md` and a MkDocs site via scripts.

## Owner's Workflow (How Updates Happen)

There are **two input sources**, both processed by the automation pipeline:

### 1. Automatic arXiv Crawl
- Runs daily (cron) via `python automation/main.py --mode daily`
- Fetches papers from configured arXiv categories + keyword filters
- LLM classifies each paper into a category and generates a 2-sentence summary
- Creates GitHub Issues for human review (one Issue per category batch)

### 2. Manual Inbox (owner-submitted links)
- A pinned GitHub Issue titled **"📥 Paper Inbox"** acts as a whiteboard
- Owner pastes arXiv URLs into comments on that Issue whenever they spot an interesting paper
- The daily pipeline also reads this Issue, processes new links the same way as crawled papers
- Processed comments get a 👍 reaction as acknowledgement
- The Issue stays open indefinitely — `processed_ids` in state ensures no double-processing

### Review & Approval
- After classification, each batch appears as a GitHub Issue with numbered papers
- Owner reviews and replies with commands: `/approve all`, `/approve 1,3`, `/reject 2`, `/edit 1 venue=ICSE 2026`
- Only comments from the configured `reviewer` (set in `config.yaml`) are trusted
- `python automation/main.py --mode finalize` (runs hourly via cron) polls for approvals, writes YAML, and pushes

### Deployment
- The pipeline runs **on a server** (not GitHub Actions) with persistent local state
- `automation/state/processed.json` tracks processed/rejected IDs and pending Issues
- After YAML is updated, `render_papers.py` rebuilds README blocks and `update_papers_badge.py` updates the paper count badge, then changes are committed and pushed
- GitHub Pages picks up the push and redeploys the docs site automatically

## Automation Pipeline Architecture

```
automation/
  main.py              # Orchestrator — modes: daily | finalize | setup | backfill
  config.yaml          # Categories, keywords, arXiv settings, LLM settings
  config_loader.py     # Cached config loader (lru_cache)
  state_manager.py     # Reads/writes automation/state/processed.json
  crawler/
    arxiv.py           # Fetches papers from arXiv by category + date + keyword filter
  inbox/
    reader.py          # Reads user-submitted links from the Inbox GitHub Issue
  enricher/
    papers_with_code.py  # Looks up GitHub repo URL via Papers With Code API
    metadata.py          # Extracts venue from abstract; falls back to "arXiv YYYY/MM"
  classifier/
    llm.py             # LiteLLM-based classifier: relevant? category? tags? summary?
  review/
    github.py          # Thin GitHub REST API wrapper (Issues, comments, reactions)
    create_issues.py   # Groups papers by category, creates one GitHub Issue per group
    poll_approvals.py  # Parses /approve /reject /edit commands from reviewer comments
  finalizer/
    yaml_writer.py     # Appends approved papers to data/papers_{category}.yaml
    git_push.py        # Runs render scripts, commits, and pushes to origin

scripts/
  render_papers.py         # Rewrites <!-- START PAPERS:X --> blocks in README.md
  update_papers_badge.py   # Updates the paper count SVG badge
  generate_ack_badges.py   # Generates acknowledgement badges
```

## Data Layout

- `data/papers_{category}.yaml` — one file per category (e.g. `papers_code_generation.yaml`)
- Category keys are defined in `automation/config.yaml` under `categories:`
- README uses `<!-- START PAPERS:{category} --> ... <!-- END PAPERS:{category} -->` markers
- `render_papers.py` replaces marker content from the corresponding YAML file

## Key Config

- `automation/config.yaml` — arXiv categories, keywords, LLM settings, reviewer GitHub username
- `automation/.env` — secrets: `GITHUB_TOKEN`, `LITELLM_BASE_URL`, `LITELLM_MODEL`, `LITELLM_API_KEY`
- Only the GitHub user set as `repo.reviewer` in config.yaml can approve/reject papers

## Cron Schedule (on server)

```
0 9 * * *   python automation/main.py --mode daily     # daily crawl + inbox processing
0 * * * *   python automation/main.py --mode finalize  # hourly approval polling
```

## Important Notes for Future Sessions

- **Do not use GitHub Actions** for the automation — it runs on the server intentionally (state persistence)
- `automation/state/processed.json` must be preserved across runs — never delete it
- When adding a new paper category: add key to `config.yaml`, create `data/papers_{key}.yaml`, and add `<!-- START PAPERS:{key} -->` block in `README.md`
- `save_config()` uses `yaml.dump` and will strip comments from `config.yaml` — only called once during `--mode setup`
- The `decided` dict in state uses int keys at runtime but JSON serialises them as strings — the code normalises on load
