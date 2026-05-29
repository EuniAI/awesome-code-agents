# Automation Setup Guide

## 1. Install dependencies

```bash
pip install -r automation/requirements.txt
```

## 2. Configure credentials

```bash
cp automation/.env.example automation/.env
# Edit automation/.env and fill in:
#   LITELLM_BASE_URL  — your LiteLLM proxy URL
#   LITELLM_MODEL     — model name as configured in your proxy
#   GITHUB_TOKEN      — Fine-grained PAT (Issues read/write on EuniAI/awesome-code-agents)
```

## 3. Create the inbox GitHub Issue (one-time)

```bash
python automation/main.py --mode=setup
```

This creates a pinned "📥 Paper Inbox" issue and saves its number to `automation/config.yaml`.
After running, go to GitHub and **pin** that issue so it's easy to find.

## 4. Set up cron jobs

```bash
crontab -e
```

Add these two lines (adjust path):

```
# Daily: crawl arXiv + process inbox → classify → open review Issues
0 9 * * *  cd /path/to/awesome-code-agents && python automation/main.py --mode=daily >> /tmp/aca-daily.log 2>&1

# Hourly: check for /approve commands → write YAML → push
0 * * * *  cd /path/to/awesome-code-agents && python automation/main.py --mode=finalize >> /tmp/aca-finalize.log 2>&1
```

## 5. Daily workflow (for you)

1. **Add papers manually** → comment arXiv links on the inbox Issue, e.g.:
   ```
   https://arxiv.org/abs/2501.12345
   ```

2. **Check review Issues** → GitHub will notify you of new `[YYYY-MM-DD]` Issues
   - Comment `/approve all` or `/approve 1,3 /reject 2`
   - To fix a field before approving: `/edit 2 category=code_generation`

3. **Pipeline does the rest** → within the hour, approved papers are written to YAML,
   README is rebuilt, and changes are pushed.

## 6. Backfill historical dates

```bash
python automation/main.py --mode=backfill --from 2025-05-01 --to 2025-05-15
```

## 7. Keyword tuning

Edit `automation/config.yaml` → `arxiv.keywords` to add/remove filter terms.
Changes take effect on the next daily run.
