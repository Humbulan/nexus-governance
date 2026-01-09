#!/bin/bash
while true; do
  if ! pgrep -f "urban_gateway_with_settlement.py" > /dev/null; then
    echo "⚠️ Gateway down! Restarting Imperial Engine..."
    python3 ~/humbu_community_nexus/urban_gateway_with_settlement.py &
  fi
  sleep 30
done
