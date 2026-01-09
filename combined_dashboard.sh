#!/bin/bash
echo "🏛️ HUMBU IMPERIAL - COMBINED REVENUE DASHBOARD"
echo "=============================================="
echo "Timestamp: $(date)"
echo ""

# RURAL REVENUE
RURAL_TX=$(grep -c "POST / HTTP" ~/humbu-rural-bot-core/humbu-rural-bot-core/scripts/gateway.log 2>/dev/null || echo "0")
RURAL_REV=$(echo "$RURAL_TX * 8.5" | bc 2>/dev/null || echo "0")

# URBAN REVENUE (from urban database)
URBAN_TX=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db "SELECT COUNT(*) FROM urban_transactions WHERE date(timestamp) = date('now')" 2>/dev/null || echo "0")
URBAN_REV=$(echo "$URBAN_TX * 12.5" | bc 2>/dev/null || echo "0")

# COMBINED
TOTAL_TX=$((RURAL_TX + URBAN_TX))
TOTAL_REV=$(echo "$RURAL_REV + $URBAN_REV" | bc 2>/dev/null || echo "0")

echo "📊 SECTOR PERFORMANCE:"
echo "----------------------"
echo "🏞️ VHEMBE (RURAL):"
echo "   • Transactions: $RURAL_TX"
echo "   • Revenue: R$RURAL_REV"
echo "   • Rate: R8.50/tx"
echo ""
echo "🏙️ GAUTENG (URBAN):"
echo "   • Transactions: $URBAN_TX"
echo "   • Revenue: R$URBAN_REV"
echo "   • Rate: R12.50/tx"
echo ""
echo "🏛️ IMPERIAL TOTAL:"
echo "   • Total Transactions: $TOTAL_TX"
echo "   • Total Revenue: R$TOTAL_REV"
echo "   • Average Rate: R$(echo "scale=2; $TOTAL_REV / $TOTAL_TX" | bc 2>/dev/null || echo "0")/tx"
echo ""
echo "📈 POTENTIAL ANALYSIS:"
echo "   • Rural Capacity: 59.5% of R1M target"
echo "   • Urban Capacity: 0% of R5M target"
echo "   • Combined Potential: R6M/month"
echo ""
echo "🌐 ACCESS POINTS:"
echo "   • Rural Gateway: http://localhost:8083"
echo "   • Urban Gateway: http://localhost:8084"
echo "   • Combined Dashboard: http://localhost:8088"
