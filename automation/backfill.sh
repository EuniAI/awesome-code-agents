#!/bin/bash
# Backfill script: 2025-10 to 2026-05
# Runs month by month, logs to automation/logs/backfill.log
# Usage: bash automation/backfill.sh

set -e
REPO=/sdb-disk/zhaoyang/awesome-code-agents
PYTHON=/Data/zhaoyang/miniconda3/bin/python
LOG=$REPO/automation/logs/backfill.log

mkdir -p $REPO/automation/logs
cd $REPO

months=(
  "2025-10-01 2025-10-31"
  "2025-11-01 2025-11-30"
  "2025-12-01 2025-12-31"
  "2026-01-01 2026-01-31"
  "2026-02-01 2026-02-28"
  "2026-03-01 2026-03-31"
  "2026-04-01 2026-04-30"
  "2026-05-01 2026-05-29"
)

echo "====== Backfill started at $(date) ======" | tee -a $LOG

for range in "${months[@]}"; do
  FROM=$(echo $range | awk '{print $1}')
  TO=$(echo $range | awk '{print $2}')
  echo "" | tee -a $LOG
  echo ">>> Backfill $FROM → $TO  ($(date))" | tee -a $LOG
  $PYTHON automation/main.py --mode backfill --from $FROM --to $TO 2>&1 | tee -a $LOG
  echo "<<< Done $FROM → $TO  ($(date))" | tee -a $LOG
  # 每月之间稍作停顿，避免 arXiv 限流
  sleep 10
done

echo "" | tee -a $LOG
echo "====== Backfill finished at $(date) ======" | tee -a $LOG
