#!/bin/bash
echo "🏙️ HUMBU AUTOMATED NIGHTLY SURGE SCHEDULER"
echo "=========================================="
echo "Business: HUMBU AI PLATFORM"
echo "Target: R5,000 daily cash flow"
echo ""

# Calculate tonight's start time (21:00)
TODAY=$(date +%Y-%m-%d)
TONIGHT_START="${TODAY} 21:00:00"
TONIGHT_START_EPOCH=$(date -d "$TONIGHT_START" +%s)
NOW_EPOCH=$(date +%s)

if [ $NOW_EPOCH -lt $TONIGHT_START_EPOCH ]; then
    WAIT_SECONDS=$((TONIGHT_START_EPOCH - NOW_EPOCH))
    WAIT_HOURS=$((WAIT_SECONDS / 3600))
    WAIT_MINUTES=$(((WAIT_SECONDS % 3600) / 60))
    
    echo "⏰ NEXT SURGE: Tonight at 21:00"
    echo "   (in $WAIT_HOURS hours $WAIT_MINUTES minutes)"
    echo ""
    echo "💰 CURRENT DAILY TARGET: R5,000"
    echo "   • Transactions needed: 400"
    echo "   • Time required: ~2 hours"
    echo "   • Hourly rate: R2,500"
    echo ""
    echo "💳 PROJECTED TOMORROW MORNING:"
    echo "   05:00 - Auto-settlement to Absa"
    echo "   08:00 - Check Absa App for R5,000"
    echo "   09:00 - ATM withdrawal ready"
else
    echo "🚀 STARTING NIGHTLY SURGE NOW"
    echo "Duration: 2 hours (400 transactions)"
    echo "Target: R5,000"
    echo ""
    
    # Start surge for 2 hours
    timeout 7200 python3 ~/humbu_community_nexus/urban_nightly_surge.py
    
    echo ""
    echo "🏁 SURGE COMPLETE"
    echo "Auto-settling to Absa..."
    ~/humbu_community_nexus/dawn_settlement.sh
fi

echo ""
echo "📱 MONITORING:"
echo "• Check balance: check-wealth"
echo "• Monitor logs: tail -f gateway_settlement.log"
echo "• Check Absa App for deposits"
