#!/bin/bash
# Setup Imperial Herald Cron Jobs

cd ~/humbu_community_nexus

# Remove existing herald cron jobs
crontab -l 2>/dev/null | grep -v "herald_scheduler" | crontab -

# Add new cron jobs
(crontab -l 2>/dev/null; echo "0 5 * * * cd ~/humbu_community_nexus && ./herald_scheduler.sh") | crontab -
(crontab -l 2>/dev/null; echo "0 18 * * * cd ~/humbu_community_nexus && ./herald_scheduler.sh") | crontab -

echo "✅ Imperial Herald Cron Jobs Installed:"
echo "   • 05:00 AM - Morning Farmer Broadcast"
echo "   • 18:00 PM - Evening IDC Audit"
echo ""
echo "📊 To verify: crontab -l"
echo "📁 Logs will be in terminal output"
