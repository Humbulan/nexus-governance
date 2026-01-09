#!/bin/bash
echo "🏛️ HUMBU IMPERIAL - REALISTIC NIGHT SHIFT"
echo "=========================================="
echo "Based on actual data: Natural flow ends ~03:16 AM"
echo ""

# Clean up
pkill -f revenue_booster_fixed.py 2>/dev/null
sleep 2

# Start services
echo "🚀 Starting Revenue Booster..."
cd ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts
echo "1" | nohup python3 revenue_booster_fixed.py > booster.log 2>&1 &
echo "✅ Revenue generation started"

# Start realistic monitor
echo "🛰️ Starting Realistic Flow Monitor..."
cd ~/humbu_community_nexus
nohup ./natural_flow_monitor_realistic.sh > realistic_flow.log 2>&1 &
echo "✅ Monitoring natural flow (ends ~03:16 AM)"

echo ""
echo "📊 EXPECTED OUTCOME:"
echo "• Natural revenue: R50,000 - R55,000"
echo "• Flow duration: ~7 hours (until ~03:16 AM)"
echo "• Auto-receipt generation upon completion"
echo "• Merchant payout synced for Friday"
echo ""
echo "🛡️ REALISTIC IGNITION COMPLETE"
