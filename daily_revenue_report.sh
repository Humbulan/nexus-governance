#!/bin/bash
# HUMBU NEXUS - REVENUE INTELLIGENCE REPORT
echo "📊 DAILY REVENUE REPORT - $(date '+%Y-%m-%d %H:%M:%S')"
echo "================================================="

# Get gateway status
status=$(curl -s http://localhost:8083/ 2>/dev/null)

if [ -n "$status" ]; then
    # Improved parsing for Gateway v2 JSON
    tx_today=$(echo "$status" | python3 -c "import sys, json; print(json.load(sys.stdin).get('transactions_today', 0))")
    rev_today=$(echo "$status" | python3 -c "import sys, json; print(json.load(sys.stdin).get('revenue_today', 0))")

    echo "💰 TODAY'S PERFORMANCE (GATEWAY v2):"
    echo "• Transactions: $tx_today"
    echo "• Revenue Generated: R$rev_today"
    
    # Calculate Math securely
    avg_tx=$(echo "scale=2; $rev_today / $tx_today" | bc 2>/dev/null || echo "0")
    monthly=$(echo "$rev_today * 30" | bc)
    progress=$(echo "scale=1; ($monthly / 1000000) * 100" | bc 2>/dev/null || echo "0")

    echo "• Average/TX: R$avg_tx"
    echo ""
    echo "📈 PROJECTIONS:"
    echo "• Projected Monthly: R$monthly"
    echo "• Target Progress: $progress% (of R1M Goal)"

    # Update the IDC Audit Trail
    summary_file="$HOME/humbu_community_nexus/daily_summary_$(date +%Y%m%d).txt"
    echo "[$(date '+%H:%M:%S')] Revenue: R$rev_today | Monthly Est: R$monthly | Progress: $progress%" >> "$summary_file"
else
    echo "❌ Gateway Offline"
fi
echo "================================================="
