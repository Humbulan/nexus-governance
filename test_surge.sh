#!/bin/bash
# 🧪 Test Surge Dashboard - Local Version
# CEO: Humbulani Mudau

cd ~/humbu_community_nexus

echo "🧪 TESTING SURGE DASHBOARD SYSTEM"
echo "================================="
echo "CEO: Humbulani Mudau"
echo "Time: $(date '+%H:%M:%S')"
echo "Location: $(pwd)"
echo ""

echo "1. File Status:"
ls -la surge_dashboard.html surge.html 2>/dev/null | grep -E "surge|html"

echo ""
echo "2. Server Routes:"
grep -n "'/surge'" multi_dashboard_server.py

echo ""
echo "3. Server Process:"
if pgrep -f "multi_dashboard_server.py" > /dev/null; then
    echo "✅ Server running"
    ps aux | grep multi_dashboard | grep -v grep | awk '{print "   PID:", $2, "| Started:", $9}'
else
    echo "❌ Server not running"
fi

echo ""
echo "4. Quick URL Test:"
echo "   Testing: https://monitor.humbu.store/surge"
status=$(curl -s -o /dev/null -w "%{http_code}" "https://monitor.humbu.store/surge")
echo "   Status: HTTP $status"

if [ "$status" = "200" ]; then
    echo ""
    echo "5. Content Preview:"
    curl -s "https://monitor.humbu.store/surge" | grep -o "<title>[^<]*</title>\|CEO.*Mudau\|R[0-9,.]*" | head -5
fi

echo ""
echo "🎯 TEST COMPLETE"
echo "💰 Daily Revenue: R3454.87"
echo "🌐 URL: https://monitor.humbu.store/surge"
