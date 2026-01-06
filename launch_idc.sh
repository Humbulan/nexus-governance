#!/bin/bash
echo "🚀 IDC PRESENTATION LAUNCHER"
echo "============================"
echo "Starting legacy dashboards..."

# Kill everything first
pkill -f "python.*http.server" 2>/dev/null
sleep 1

# Start unified hub
cd ~/humbu_community_nexus
python3 -m http.server 8088 --bind 127.0.0.1 &
SERVER_PID=$!
sleep 3

# Check if server started
if kill -0 $SERVER_PID 2>/dev/null; then
    echo "✅ Legacy Hub: http://localhost:8088"
    
    # Show available dashboards
    echo ""
    echo "📁 AVAILABLE DASHBOARDS:"
    echo "1. Navigation Hub: http://localhost:8088/legacy_navigation.html"
    echo "2. Logistics Map: http://localhost:8088/logistics_live_map.html"
    echo "3. Financial Command: http://localhost:8088/index_financial_command.html"
    echo "4. Community Portal: http://localhost:8088/dashboard_index_fixed.html"
    echo "5. Master Portal: http://localhost:8088/master_portal.html"
    
    # Start tunnel if not running
    if ! pgrep -f cloudflared > /dev/null; then
        echo ""
        echo "🌐 Starting public tunnel..."
        cloudflared tunnel run --url http://localhost:8088 humbu-imperial &
        sleep 3
    fi
    
    echo ""
    echo "🌐 PUBLIC URL: monitor.humbu.store"
    echo ""
    echo "🏛️ IDC TALKING POINTS:"
    echo "• 708 Community Members"
    echo "• 17 Active Vehicles (Live Map)"
    echo "• $47,574.56 Daily Revenue"
    echo "• R412,730.15 Industrial Backing"
    echo "• R9,084,769 April 2026 Forecast"
    
    echo ""
    echo "📱 OPEN IN BROWSER: http://localhost:8088/legacy_navigation.html"
else
    echo "❌ Failed to start server"
fi
