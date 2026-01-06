#!/bin/bash
# HUMBU NEXUS - AVIATION INTELLIGENCE SCRAPER
LOG_FILE="/data/data/com.termux/files/home/logs/imperial_server.log"

while true; do
  # Check if log exists, scrape CARGO_VAL, or default to 125000
  if [ -f "$LOG_FILE" ]; then
    LATEST_CARGO=$(grep "CARGO_VAL" "$LOG_FILE" | tail -1 | awk -F'=' '{print $2}')
  fi
  
  # If LATEST_CARGO is empty, use the baseline
  if [ -z "$LATEST_CARGO" ]; then LATEST_CARGO="125000"; fi
  
  echo "$LATEST_CARGO" > ~/humbu_community_nexus/api/.air_cache
  sleep 15
done
