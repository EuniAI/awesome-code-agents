# _legacy (temporary)

Parked pre-refactor automation pipeline. NOT live code: cron is stopped and nothing
imports from here. We rebuild the pipeline fresh as flat modules under `automation/`,
copying the still-good logic (arxiv fetch, GitHub API, inbox reader, venue extraction)
from here rather than rewriting it from memory. After a completeness diff against this
folder, delete `_legacy/` entirely.
