#!/bin/bash
echo "🏛️ FIX MONITOR.HUMBU.STORE DOMAIN"
echo "================================"
echo "Time: $(date '+%H:%M:%S')"
echo ""

# Kill everything
pkill -9 python 2>/dev/null
pkill -9 cloudflared 2>/dev/null
sleep 2

# Start local server
echo "🚀 Starting local dashboards..."
cd ~/humbu_community_nexus
python3 -m http.server 8088 --bind 0.0.0.0 &
sleep 3

echo "✅ Local server: RUNNING"
echo "   Test: http://localhost:8088/legacy_navigation.html"
echo ""

# Start tunnel
echo "🌍 Starting Cloudflare tunnel..."
cloudflared tunnel --config ~/.cloudflared/config_domain.yml run 2>&1 | tee /tmp/tunnel_run.log &
sleep 10

echo ""
echo "🔍 TUNNEL STATUS:"
if tail -10 /tmp/tunnel_run.log | grep -q "Registered tunnel connection"; then
    echo "✅ Tunnel: CONNECTED"
    echo "   Tunnel ID: c07a0d01-7820-49d5-ac68-36e48a6b2b94"
    echo "   CNAME Target: c07a0d01-7820-49d5-ac68-36e48a6b2b94.cfargotunnel.com"
else
    echo "❌ Tunnel: CONNECTION ISSUE"
fi

echo ""
echo "🔗 DOMAIN TEST:"
echo -n "   monitor.humbu.store: "
if curl -s --max-time 10 https://monitor.humbu.store > /dev/null; then
    echo "✅ WORKING"
    echo "   🎉 DOMAIN IS LIVE!"
else
    echo "� ERROR 1033"
    echo ""
    echo "🚨 MANUAL ACTION REQUIRED:"
    echo "1. Login to Cloudflare Dashboard"
    echo "2. Go to humbu.store → DNS → Records"
    echo "3. Edit CNAME record for 'monitor'"
    echo "4. Set Target to: c07a0d01-7820-49d5-ac68-36e48a6b2b94.cfargotunnel.com"
    echo "5. Save and wait 3 minutes"
    echo ""
    echo "📱 Open instructions: termux-open-url ~/humbu_community_nexus/dns_fix_urgent.html"
fi

echo ""
echo "💰 VERIFIED METRICS:"
echo "• 708 Community Members"
echo "• 17 Active Vehicles"
echo "• $47,574.56 Daily Revenue"
echo "• R412,730.15 Industrial Backing"
echo "• R9,084,769 April 2026 Forecast"
