#!/bin/bash
while true; do
    clear
    echo "🏙️ GAUTENG URBAN STRESS TEST - LIVE DASHBOARD"
    echo "============================================="
    echo "Time: $(date +%H:%M:%S)"
    echo ""
    
    # Urban Gateway Status
    echo "🌉 URBAN GATEWAY STATUS:"
    GATEWAY_STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8084/ 2>/dev/null || echo "000")
    if [ "$GATEWAY_STATUS" = "200" ]; then
        echo "   ✅ ONLINE (Port 8084)"
    else
        echo "   ❌ OFFLINE"
    fi
    
    # Urban Database Stats
    echo ""
    echo "💾 URBAN DATABASE:"
    URBAN_TX=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db "SELECT COUNT(*) FROM urban_transactions;" 2>/dev/null || echo "0")
    URBAN_REV=$(echo "$URBAN_TX * 12.5" | bc 2>/dev/null || echo "0")
    echo "   • Transactions: $URBAN_TX"
    echo "   • Revenue: R$URBAN_REV"
    echo "   • Rate: R12.50/tx"
    
    # Node Distribution
    echo ""
    echo "🗺️ URBAN NODE DISTRIBUTION:"
    sqlite3 ~/humbu_community_nexus/urban_gateway.db << 'SQL_EOF'
SELECT 
    urban_node,
    COUNT(*) as tx_count,
    COUNT(*) * 12.5 as revenue,
    printf('%.1f', (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM urban_transactions))) || '%' as percentage
FROM urban_transactions 
GROUP BY urban_node 
ORDER BY tx_count DESC;
SQL_EOF
    
    # Performance Metrics
    echo ""
    echo "📈 PERFORMANCE METRICS:"
    if [ $URBAN_TX -gt 0 ]; then
        # Calculate rate based on test duration
        TEST_DURATION=$(( $(date +%s) - $(stat -c %Y ~/humbu_community_nexus/urban_stress_test.log 2>/dev/null || echo $(date +%s)) ))
        if [ $TEST_DURATION -gt 0 ]; then
            TX_PER_MIN=$(echo "scale=1; ($URBAN_TX * 60) / $TEST_DURATION" | bc 2>/dev/null || echo "0")
            REV_PER_MIN=$(echo "scale=2; ($URBAN_REV * 60) / $TEST_DURATION" | bc 2>/dev/null || echo "0")
            echo "   • Rate: $TX_PER_MIN tx/min"
            echo "   • Revenue Rate: R$REV_PER_MIN/min"
            echo "   • Projected Hourly: R$(echo "$REV_PER_MIN * 60" | bc 2>/dev/null || echo "0")"
        fi
    fi
    
    # Stress Test Progress
    echo ""
    echo "⏱️ TEST PROGRESS:"
    echo "   • Elapsed: $(( $(date +%s) - $(stat -c %Y ~/humbu_community_nexus/urban_stress_test.log 2>/dev/null || echo $(date +%s)) )) seconds"
    echo "   • Target: 100 transactions"
    echo "   • Progress: $URBAN_TX/100"
    
    # Progress Bar
    if [ $URBAN_TX -gt 0 ]; then
        PERCENT=$((URBAN_TX))
        BAR="["
        for i in {1..50}; do
            if [ $i -le $((PERCENT / 2)) ]; then
                BAR="${BAR}█"
            else
                BAR="${BAR}░"
            fi
        done
        BAR="${BAR}]"
        echo "   $BAR ${PERCENT}%"
    fi
    
    echo ""
    echo "Press Ctrl+C to exit"
    sleep 5
done
