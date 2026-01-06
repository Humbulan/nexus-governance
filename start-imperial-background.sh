#!/bin/bash
# 🏛️ SIMPLE BACKGROUND STARTER
echo "🚀 Starting Imperial background services..."

# Start dashboard service
if [ ! -f ~/humbu_community_nexus/services/dashboard.pid ] || ! ps -p $(cat ~/humbu_community_nexus/services/dashboard.pid) > /dev/null; then
    echo "📊 Starting dashboard service..."
    nohup ~/humbu_community_nexus/services/imperial-dashboard.service.sh > /dev/null 2>&1 &
    echo $! > ~/humbu_community_nexus/services/dashboard.pid
    echo "✅ Dashboard service started (PID: $!)"
else
    echo "📊 Dashboard service already running"
fi

# Start tunnel service
if [ ! -f ~/humbu_community_nexus/services/tunnel.pid ] || ! ps -p $(cat ~/humbu_community_nexus/services/tunnel.pid) > /dev/null; then
    echo "🌐 Starting tunnel service..."
    nohup ~/humbu_community_nexus/services/imperial-tunnel.service.sh > /dev/null 2>&1 &
    echo $! > ~/humbu_community_nexus/services/tunnel.pid
    echo "✅ Tunnel service started (PID: $!)"
else
    echo "🌐 Tunnel service already running"
fi

echo ""
echo "🎯 SERVICES ACTIVE:"
echo "   Dashboard: http://localhost:8088"
echo "   Public: https://monitor.humbu.store"
echo ""
echo "💡 Commands:"
echo "   imperial-status   - Check service status"
echo "   imperial-stop     - Stop all services"
echo ""
echo "🏛️ Imperial background services started at $(date '+%H:%M:%S')"
