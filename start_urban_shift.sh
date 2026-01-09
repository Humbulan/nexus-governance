#!/bin/bash
echo "🏙️ STARTING GAUTENG URBAN SHIFT"
echo "================================"
echo "Time: $(date)"
echo ""

# 1. Activate Urban Bridge
echo "🌉 Activating Urban Bridge..."
humbu-bridge-gp
sleep 3

# 2. Start Urban Booster
echo "🚀 Starting Urban Revenue Booster..."
cd ~/humbu_community_nexus
nohup python3 urban_revenue_booster.py <<< "4" > urban_booster.log 2>&1 &
URBAN_PID=$!
sleep 2

if kill -0 $URBAN_PID 2>/dev/null; then
    echo "✅ Urban Booster Active (PID: $URBAN_PID)"
    echo "   • Rate: R12.50/tx"
    echo "   • Mode: Continuous"
    echo "   • Log: ~/humbu_community_nexus/urban_booster.log"
else
    echo "❌ Urban Booster failed to start"
fi

# 3. Show status
echo ""
echo "📊 URBAN SYSTEM STATUS:"
humbu-urban-status

echo ""
echo "🏙️ GAUTENG URBAN SHIFT ACTIVE"
echo "Expected Revenue: R642,637.50+"
