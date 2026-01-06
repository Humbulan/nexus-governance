#!/bin/bash
while true; do
  # CHECK AVIATION (1808)
  (echo > /dev/tcp/127.0.0.1/1808) >/dev/null 2>&1
  if [ $? -ne 0 ]; then
    echo "⚠️ [WATCHDOG] Aviation Down. Restarting..."
    cd ~/humbu_community_nexus
    nohup python3 -m http.server 1808 --bind 0.0.0.0 > ~/logs/aviation.log 2>&1 &
  fi

  # CHECK REVENUE GATEWAY (8083)
  (echo > /dev/tcp/127.0.0.1/8083) >/dev/null 2>&1
  if [ $? -ne 0 ]; then
    echo "⚠️ [WATCHDOG] Revenue Gateway Down. Restarting..."
    cd ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts
    nohup python3 humbu_gateway_fixed.py > gateway.log 2>&1 &
  fi
  
  sleep 30
done
