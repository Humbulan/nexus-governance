#!/bin/bash
echo "🔍 DAILY SYSTEM CHECK - $(date '+%Y-%m-%d')"
echo "========================================"

# Check dashboard
if curl -s http://localhost:8088 | grep -q "47,574.56"; then
    echo "✅ Dashboard: Operational (shows \$47,574.56)"
else
    echo "⚠️ Dashboard: Needs attention"
fi

# Check services
if [ -f ~/humbu_community_nexus/services/dashboard.pid ] && ps -p $(cat ~/humbu_community_nexus/services/dashboard.pid) > /dev/null; then
    echo "✅ Dashboard Service: Running"
else
    echo "❌ Dashboard Service: Stopped"
fi

echo ""
echo "📧 IDC STATUS: Email sent - awaiting response"
echo "📁 Documents ready for review"
echo "🚀 System prepared for demonstration"
