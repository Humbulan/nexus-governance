#!/bin/bash
while true; do
  if ! curl -s --max-time 5 http://localhost:8082/ > /dev/null; then
    echo "$(date): ❌ Server down, restarting..." >> ~/server_health.log
    pkill -f "multi_dashboard_server.py"
    cd ~/humbu_community_nexus
    nohup python3 multi_dashboard_server.py > ~/.imperial_portal.log 2>&1 &
  fi
  sleep 60
done
