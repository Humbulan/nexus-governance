#!/bin/bash
echo "⚡ QUICK REVIVE PROTOCOL"
echo "========================"
echo "Killing all python processes..."
pkill -9 python 2>/dev/null
sleep 2

echo "Starting Unified Hub (port 8088)..."
cd ~/humbu_community_nexus
python3 -m http.server 8088 --bind 127.0.0.1 &
sleep 3

echo "Testing connection..."
if curl -s http://localhost:8088 > /dev/null; then
    echo "✅ Unified Hub: ACTIVE"
    echo "🌐 Public: monitor.humbu.store"
    echo ""
    echo "📊 KEY DASHBOARDS:"
    echo "• monitor.humbu.store/legacy_navigation.html"
    echo "• monitor.humbu.store/logistics_live_map.html"
    echo "• monitor.humbu.store/index_financial_command.html"
else
    echo "❌ Failed to start"
fi
