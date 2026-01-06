#!/bin/bash
# 🏛️ Imperial Tunnel Service - Background Runner
echo "🌐 Imperial Tunnel Service starting at $(date '+%H:%M:%S')" > ~/humbu_community_nexus/logs/tunnel-service-start.log

while true; do
    TIMESTAMP=$(date '+%H:%M:%S')
    
    # Check if tunnel is working
    if ! curl -s https://monitor.humbu.store > /dev/null 2>&1; then
        echo "$TIMESTAMP - Tunnel not responding, restarting..." >> ~/humbu_community_nexus/logs/tunnel-service.log
        pkill -f cloudflared 2>/dev/null
        sleep 3
        nohup cloudflared tunnel --url http://localhost:8088 run c07a0d01-7820-49d5-ac68-36e48a6b2b94 >> ~/humbu_community_nexus/logs/cloudflared.log 2>&1 &
        echo "$TIMESTAMP - Tunnel restart initiated" >> ~/humbu_community_nexus/logs/tunnel-service.log
    else
        echo "$TIMESTAMP - Tunnel OK" >> ~/humbu_community_nexus/logs/tunnel-service.log
    fi
    
    sleep 60  # Check every minute
done
