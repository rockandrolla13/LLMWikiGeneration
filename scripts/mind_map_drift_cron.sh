#!/usr/bin/env bash
#
# Weekly MIND_MAP drift check, run from cron.
#
# Appends to the log ONLY when drift exceeds the threshold. A weekly job that
# reports every week stops being read by week three, so silence is the point:
# a new entry in this log means new sources have landed that the curated map
# does not reach.
#
# This script and the Python it calls write nothing to the wiki. MIND_MAP.md is
# curated by hand and no job may touch it.
#
# Install:  crontab -l | { cat; echo "47 8 * * 1 $PWD/scripts/mind_map_drift_cron.sh"; } | crontab -
# Inspect:  cat ~/wiki-mindmap-drift.log
# Remove:   crontab -e   (delete the line)

set -uo pipefail

REPO="/media/ak/10E1026C4FA6006E/GitRepos/LLMWikiGeneration"
PYTHON="/home/ak/anaconda3/bin/python3"
LOG="$HOME/wiki-mindmap-drift.log"

# Threshold is set to the count measured on 2026-08-09. The job stays silent
# until MORE sources drift off the map than were already off it. Lower it after
# a curation session, or the job will not speak again until drift re-accumulates.
THRESHOLD=96

# cd matters: source_path values in this vault resolve relative to the repo root,
# and cron does not inherit a working directory.
cd "$REPO" || {
    echo "[$(date -Is)] FAILED: cannot cd to $REPO" >> "$LOG"
    exit 2
}

OUTPUT=$("$PYTHON" scripts/mind_map_drift.py --threshold "$THRESHOLD" --limit 15 2>&1)
STATUS=$?

case "$STATUS" in
    0)  exit 0 ;;                       # within threshold, stay quiet
    1)  {
            echo "=============================================================="
            echo "[$(date -Is)] MIND_MAP drift above $THRESHOLD sources"
            echo "=============================================================="
            echo "$OUTPUT"
            echo
        } >> "$LOG"
        ;;
    *)  {
            echo "[$(date -Is)] drift check FAILED (exit $STATUS)"
            echo "$OUTPUT"
            echo
        } >> "$LOG"
        ;;
esac
