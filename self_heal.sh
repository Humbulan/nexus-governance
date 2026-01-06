#!/bin/bash
# 🛡️ HUMBU IMPERIAL: SELF-HEALING PROTOCOL
URL="https://monitor.humbu.store"

while true; do
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
    
    if; then
        echo "[$(date)] ✅ SYSTEM HEALTHY (200 OK)"
    else
        echo "[$(date)] 🚨 ALERT: STATUS $STATUS. INITIATING RECOVERY..."
        
        # 1. Kill ghost processes
        pkill -9 -f revenue_engine.py
        pkill -f cloudflared
        sleep 2
        
        # 2. Restart Revenue Engine (Village #41 sync)
        nohup python3 ~/humbu_community_nexus/revenue_engine.py > ~/logs/engine.log 2>&1 &
        sleep 5
        
        # 3. Restart Cloudflare Tunnel
        nohup cloudflared tunnel run humbu-monitor > ~/logs/tunnel.log 2>&1 &
        
        echo "[$(date)] 🏛️ RECOVERY COMPLETE. PULSE RESTORED."
    fi
    sleep 300 # Check every 5 minutes
done
