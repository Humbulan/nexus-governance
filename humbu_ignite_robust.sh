#!/bin/bash
echo "🏛️ HUMBU IMPERIAL - ROBUST NIGHT SHIFT"
echo "======================================"
echo "Timestamp: $(date)"
echo ""

# 1. First, stop any existing processes
echo "🧹 Cleaning previous sessions..."
pkill -f revenue_booster_fixed.py 2>/dev/null
pkill -f natural_flow_monitor_realistic.sh 2>/dev/null
sleep 2

# 2. Check if gateway is running
echo "🔍 Checking Revenue Gateway..."
if ! curl -s http://localhost:8083/ > /dev/null 2>&1; then
    echo "⚠️ Gateway not running on 8083"
    echo "Starting gateway..."
    cd ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts
    nohup python3 humbu_gateway_fixed.py > gateway.log 2>&1 &
    sleep 3
fi

# 3. Start Revenue Booster with proper handling
echo "🚀 Starting Revenue Booster..."
cd ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts

# Check current transaction count
INITIAL_COUNT=$(grep -c "POST / HTTP" gateway.log 2>/dev/null || echo "0")
echo "Initial transactions: $INITIAL_COUNT"

# Start booster in background with input
{
    sleep 2
    echo "1"
} | nohup python3 revenue_booster_fixed.py > booster.log 2>&1 &
BOOSTER_PID=$!
sleep 3

if kill -0 $BOOSTER_PID 2>/dev/null; then
    echo "✅ Revenue Booster Started (PID: $BOOSTER_PID)"
    
    # Check if it's working
    sleep 2
    CURRENT_COUNT=$(grep -c "POST / HTTP" gateway.log 2>/dev/null || echo "0")
    NEW_TRANSACTIONS=$((CURRENT_COUNT - INITIAL_COUNT))
    
    if [ "$NEW_TRANSACTIONS" -gt 0 ]; then
        echo "💰 Revenue flowing: +$NEW_TRANSACTIONS transactions"
    else
        echo "⚠️ No new transactions yet - monitoring..."
    fi
else
    echo "❌ Revenue Booster failed to start"
    echo "Check: tail -f booster.log"
fi

# 4. Start Realistic Flow Monitor
echo "🛰️ Starting Realistic Flow Monitor..."
cd ~/humbu_community_nexus
nohup ./natural_flow_monitor_realistic.sh > realistic_flow.log 2>&1 &
MONITOR_PID=$!

if kill -0 $MONITOR_PID 2>/dev/null; then
    echo "✅ Flow Monitor Started (PID: $MONITOR_PID)"
    echo "   • Will detect natural endpoint"
    echo "   • Auto-generates receipt"
else
    echo "⚠️ Flow Monitor failed to start"
fi

# 5. Show expected outcome
echo ""
echo "📊 EXPECTED OUTCOME:"
echo "• Natural revenue: R50,000 - R55,000"
echo "• Flow duration: ~7 hours"
echo "• Auto-receipt upon completion"
echo ""
echo "📱 MONITOR COMMANDS:"
echo "• Check revenue: humbu-revenue"
echo "• Check status: humbu-status"
echo "• Stop early: humbu-extinguish"
echo ""
echo "🛡️ ROBUST IGNITION COMPLETE AT: $(date)"
