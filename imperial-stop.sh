#!/bin/bash
# 🏛️ STOP IMPERIAL SERVICES
echo "🛑 Stopping Imperial services..."

if [ -f ~/humbu_community_nexus/services/dashboard.pid ]; then
    kill $(cat ~/humbu_community_nexus/services/dashboard.pid) 2>/dev/null
    echo "📊 Dashboard service stopped"
fi

if [ -f ~/humbu_community_nexus/services/tunnel.pid ]; then
    kill $(cat ~/humbu_community_nexus/services/tunnel.pid) 2>/dev/null
    echo "🌐 Tunnel service stopped"
fi

# Also stop direct processes
pkill -f "imperial-dashboard.service" 2>/dev/null
pkill -f "imperial-tunnel.service" 2>/dev/null
pkill -f cloudflared 2>/dev/null
pkill -f "python3 -m http.server 8088" 2>/dev/null

echo "✅ All Imperial services stopped"
