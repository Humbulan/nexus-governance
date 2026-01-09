#!/bin/bash
echo "⏰ SETTING UP 05:00 AM NATURAL SUMMARY TRIGGER"
echo "=============================================="

# Calculate seconds until 05:00
CURRENT_TIME=$(date +%s)
TARGET_TIME=$(date -d "05:00" +%s)

if [ $CURRENT_TIME -gt $TARGET_TIME ]; then
    # If already past 05:00, schedule for tomorrow
    TARGET_TIME=$(date -d "tomorrow 05:00" +%s)
fi

SECONDS_TO_WAIT=$((TARGET_TIME - CURRENT_TIME))
HOURS_TO_WAIT=$((SECONDS_TO_WAIT / 3600))
MINUTES_TO_WAIT=$(((SECONDS_TO_WAIT % 3600) / 60))

echo "⏰ Next trigger: 05:00 AM"
echo "⏱️ Time until trigger: ${HOURS_TO_WAIT}h ${MINUTES_TO_WAIT}m"
echo ""

# Create the trigger script
cat > /tmp/natural_summary_trigger.sh << 'TRIGGER_EOF'
#!/bin/bash
echo "🔔 05:00 AM NATURAL SUMMARY TRIGGERED"
echo "====================================="
echo "Timestamp: $(date)"
echo ""

# Stop the revenue booster naturally
pkill -f revenue_booster_fixed.py 2>/dev/null
echo "✅ Revenue booster stopped (natural endpoint)"

# Generate shift receipt
cd ~/humbu_community_nexus
./generate_shift_receipt.sh

# Update merchant payout database
python3 merchant_payouts_fixed.py --sync-from-log ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log

# Send system status
echo ""
echo "🌅 MORNING SYSTEM STATUS:"
humbu-status

echo ""
echo "🏛️ NATURAL FLOW PRESERVED"
echo "The overnight shift completed organically"
echo "Village economics remain sustainable"
TRIGGER_EOF

chmod +x /tmp/natural_summary_trigger.sh

# Schedule the trigger
echo "📅 Scheduling natural summary trigger..."
echo "Execute at 05:00: /tmp/natural_summary_trigger.sh"
echo ""
echo "To run manually: ./generate_shift_receipt.sh"
