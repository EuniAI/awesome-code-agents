"""
Runs the render/badge scripts then commits and pushes all changes.
Uses --no-verify to skip pre-commit hooks (bot runs render scripts explicitly).
"""

from __future__ import annotations

import logging
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


def _run(cmd: list[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess:
    logger.debug("$ %s", " ".join(cmd))
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.stdout.strip():
        logger.debug("stdout: %s", result.stdout.strip())
    if result.stderr.strip():
        logger.debug("stderr: %s", result.stderr.strip())
    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command failed (exit {result.returncode}): {' '.join(cmd)}\n"
            f"stderr: {result.stderr.strip()}"
        )
    return result


def render_and_push(repo_root: Path, commit_message: str) -> bool:
    """
    1. Run render_papers.py  (rebuild README blocks)
    2. Run update_papers_badge.py (update paper count badge)
    3. git add data/ README.md docs/
    4. git commit --no-verify
    5. git push

    Returns True if a commit was made, False if nothing changed.
    """
    scripts = repo_root / "scripts"

    # Step 1: render README
    logger.info("Running render_papers.py…")
    _run(["python", str(scripts / "render_papers.py")], cwd=repo_root)

    # Step 2: update badge
    logger.info("Running update_papers_badge.py…")
    _run(["python", str(scripts / "update_papers_badge.py")], cwd=repo_root)

    # Step 3: check for changes
    status = _run(["git", "status", "--porcelain"], cwd=repo_root, check=False)
    if not status.stdout.strip():
        logger.info("Nothing to commit — working tree clean.")
        return False

    # Step 4: stage relevant paths
    _run(["git", "add", "data/", "README.md", "docs/"], cwd=repo_root, check=False)

    # Step 5: commit
    logger.info("Committing: %s", commit_message)
    _run(
        ["git", "commit", "--no-verify", "-m", commit_message],
        cwd=repo_root,
    )

    # Step 6: push
    logger.info("Pushing to origin…")
    _run(["git", "push"], cwd=repo_root)

    logger.info("Push successful.")
    return True
