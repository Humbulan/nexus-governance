#!/bin/bash
clear
echo "🚨 BOARD MEETING EMERGENCY OVERRIDE"
echo "==================================="
echo "CEO: Humbulani Mudau"
echo "Time: $(date)"
echo ""

echo "1. Current Server Status:"
ps aux | grep -E "(8082|9090)" | grep -v grep || echo "No servers found"

echo ""
echo "2. Force Restart Protocol:"
pkill -9 -f "python.*8082" 2>/dev/null
sleep 2
cd ~/humbu_community_nexus
nohup python3 -m http.server 8082 > /dev/null 2>&1 &
echo "✅ Clean HTTP server started on 8082"

echo ""
echo "3. Verify Essential Access:"
echo "   • Portfolio: http://localhost:9090/"
echo "   • Dashboard: http://localhost:8082/imperial-dashboard-8082.html"
echo "   • Village Data: http://localhost:8082/village_data.json"

echo ""
echo "4. Quick Test:"
curl -s http://localhost:9090/ | grep -o '"portfolio":"[^"]*"' || echo "⚠️ Portfolio check failed"

echo ""
echo "🛡️ EMERGENCY PROTOCOL COMPLETE"
echo "System is running in basic mode for board presentation."
