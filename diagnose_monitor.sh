#!/bin/bash
echo "🔍 DIAGNOSTIC FOR MONITOR.HUMBU.STORE"
echo "===================================="

echo "1. CHECKING LOCAL SERVER..."
if curl -s --max-time 5 http://localhost:8088 > /dev/null; then
    echo "✅ Local server: ACTIVE"
    echo "   URL: http://localhost:8088/legacy_navigation.html"
else
    echo "❌ Local server: DOWN"
    echo "   Starting server..."
    pkill -f "python.*http.server"
    cd ~/humbu_community_nexus
    python3 -m http.server 8088 --bind 0.0.0.0 &
    sleep 3
fi

echo ""
echo "2. CHECKING TUNNEL PROCESS..."
if pgrep -f cloudflared > /dev/null; then
    echo "✅ Cloudflared: RUNNING"
    echo "   PID: $(pgrep -f cloudflared)"
    
    # Check tunnel connections
    echo "   Connections:"
    tail -20 ~/logs/tunnel_*.log 2>/dev/null | grep "Registered tunnel" || echo "   No connection logs found"
else
    echo "❌ Cloudflared: NOT RUNNING"
    echo "   Starting tunnel..."
    nohup cloudflared tunnel run --url http://localhost:8088 humbu-imperial > ~/logs/tunnel_diagnose.log 2>&1 &
    sleep 5
fi

echo ""
echo "3. CHECKING PUBLIC ACCESS..."
echo -n "   monitor.humbu.store: "
if curl -s --max-time 10 -I monitor.humbu.store 2>/dev/null | grep -q "HTTP"; then
    echo "✅ RESPONDING"
    curl -s --max-time 5 -I monitor.humbu.store | head -5
else
    echo "❌ NO RESPONSE (Error 1033)"
    echo ""
    echo "🚨 ACTION REQUIRED:"
    echo "   This is a DNS/CNAME issue at Cloudflare."
    echo "   Either:"
    echo "   1. Wait 5-10 minutes for DNS propagation"
    echo "   2. Manually set CNAME at Cloudflare Dashboard"
    echo "   3. Use: cat ~/humbu_community_nexus/cloudflare_dns_instructions.txt"
fi

echo ""
echo "4. ALTERNATE TEST: CLOUDFLARE TUNNEL HEALTH..."
cloudflared tunnel info humbu-imperial 2>/dev/null | head -10 || echo "   Tunnel info not available"

echo ""
echo "🎯 RECOMMENDED ACTION:"
echo "   If monitor.humbu.store still shows Error 1033 after 10 minutes,"
echo "   you MUST set the CNAME manually in Cloudflare Dashboard."
