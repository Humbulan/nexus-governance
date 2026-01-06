#!/data/data/com.termux/files/usr/bin/bash

clear
echo "📊 HUMBU COMMUNITY NEXUS - LIVE DASHBOARD"
echo "🌍 Platform Status: $(date)"
echo "=========================================="

# Check if platform is running
if ps aux | grep -q "[c]ommunity_web.py"; then
    echo "✅ STATUS: PLATFORM RUNNING"
    echo "🌐 URL: http://localhost:8086"
    echo ""
    
    # Get live stats
    echo "📈 LIVE STATISTICS:"
    curl -s http://localhost:8086/api/stats 2>/dev/null | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    stats = data['stats']
    print(f'👥 Users: {stats[\"total_users\"]}')
    print(f'📦 Listings: {stats[\"market_listings\"]}')
    print(f'🎯 Tasks: {stats[\"open_tasks\"]}')
    print(f'💰 Wallet Value: R{stats[\"total_wallet_value\"]:.2f}')
except:
    print('Fetching data...')
"
else
    echo "❌ STATUS: PLATFORM STOPPED"
    echo "💡 Start with: python3 community_web.py"
fi

echo ""
echo "🚀 QUICK ACTIONS:"
echo "   1. View Web Portal: http://localhost:8086"
echo "   2. Check API: curl http://localhost:8086/api/stats"
echo "   3. Start Platform: python3 community_web.py"
echo "   4. Stop Platform: pkill -f community_web.py"
echo "   5. Generate Map: python3 community_hub.py"
echo ""
echo "🏁 Press Ctrl+C to exit this dashboard"
echo "🔄 Auto-refreshing in 30 seconds..."

sleep 30
exec $0
