#!/bin/bash
echo "🛡️ RECOVERING IMPERIAL GATEWAY..."
pkill -9 cloudflared
sleep 1
nohup cloudflared tunnel --heartbeat-interval 10s --url http://localhost:8088 --hostname monitor.humbu.store > ~/humbu_community_nexus/logs/tunnel-fix.log 2>&1 &
sleep 5
if grep -q "Registered tunnel" ~/humbu_community_nexus/logs/tunnel-fix.log; then
    echo "✅ GATEWAY RESTORED: https://monitor.humbu.store"
else
    echo "⚠️ Handshake pending... check logs in a moment."
fi
