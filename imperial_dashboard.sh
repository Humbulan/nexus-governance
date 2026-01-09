#!/bin/bash
echo "======================================================"
echo "🏛️  VHEMBE IMPERIAL NEXUS COMMAND CENTER - ENHANCED"
echo "📡  UNIFIED CASH FLOW & SYSTEM MONITORING"
echo "======================================================"
echo ""

# Get current time
echo "⏰ SYSTEM TIME: $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo ""

# SECTION 1: CASH FLOW STATUS
echo "💰 REAL-TIME CASH FLOW STATUS"
echo "============================="

# Urban Gateway Status
if curl -s http://localhost:8084/ > /dev/null 2>&1; then
    URBAN_STATUS=$(curl -s http://localhost:8084/ | python3 -c "
import json, sys
try:
    data = json.load(sys.stdin)
    unsettled = data.get('performance', {}).get('unsettled_amount', 0)
    settled = data.get('performance', {}).get('settled_amount', 0)
    print(f'✅ URBAN GATEWAY: ONLINE')
    print(f'   • Ready to Settle: R{unsettled:.2f}')
    print(f'   • Already Settled: R{settled:.2f}')
    print(f'   • Business: {data.get(\"business\", {}).get(\"name\", \"N/A\")}')
except:
    print('✅ URBAN GATEWAY: ONLINE (Detailed stats unavailable)')
")
    echo "$URBAN_STATUS"
else
    echo "❌ URBAN GATEWAY: OFFLINE"
fi

echo ""

# Rural Gateway Status
if curl -s http://localhost:8083/ > /dev/null 2>&1; then
    echo "✅ RURAL GATEWAY: ONLINE (Port 8083)"
else
    echo "❌ RURAL GATEWAY: OFFLINE"
fi

echo ""

# Database Summary
echo "📊 DATABASE SUMMARY"
DB_SUMMARY=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db << 'DB_QUERY'
SELECT 
    '• Total Transactions: ' || COUNT(*) || ' (R' || COALESCE(SUM(revenue_generated), 0) || ')',
    '• Unsettled: ' || SUM(CASE WHEN settled = 0 THEN 1 ELSE 0 END) || ' (R' || COALESCE(SUM(CASE WHEN settled = 0 THEN revenue_generated ELSE 0 END), 0) || ')',
    '• Settled: ' || SUM(CASE WHEN settled = 1 THEN 1 ELSE 0 END) || ' (R' || COALESCE(SUM(CASE WHEN settled = 1 THEN revenue_generated ELSE 0 END), 0) || ')'
FROM urban_transactions;
DB_QUERY
)

echo "$DB_SUMMARY" | while read -r line; do
    echo "  $line"
done

echo ""

# Last Settlement
LAST_SETTLE=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db "SELECT batch_id, total_amount, settled_at FROM settlement_batch WHERE status = 'COMPLETED' ORDER BY settled_at DESC LIMIT 1" 2>/dev/null)
if [ -n "$LAST_SETTLE" ]; then
    BATCH_ID=$(echo "$LAST_SETTLE" | cut -d'|' -f1)
    AMOUNT=$(echo "$LAST_SETTLE" | cut -d'|' -f2)
    TIME=$(echo "$LAST_SETTLE" | cut -d'|' -f3 | cut -d'T' -f1)
    echo "📅 LAST SETTLEMENT:"
    echo "  • Batch: $BATCH_ID"
    echo "  • Amount: R$AMOUNT"
    echo "  • Date: $TIME"
fi

echo ""

# SECTION 2: SYSTEM HEALTH
echo "🩺 SYSTEM HEALTH STATUS"
echo "======================"

# Port Checks
PORTS="8084 8083 11434 8088"
for PORT in $PORTS; do
    if nc -z localhost $PORT 2>/dev/null; then
        echo "✅ Port $PORT: LISTENING"
    else
        echo "❌ Port $PORT: CLOSED"
    fi
done

echo ""

# Process Checks
echo "⚙️ RUNNING PROCESSES:"
if pgrep -f "urban_gateway" > /dev/null; then
    URBAN_PID=$(pgrep -f "urban_gateway")
    echo "  • Urban Gateway: PID $URBAN_PID"
fi

if pgrep -f "revenue_gateway" > /dev/null; then
    RURAL_PID=$(pgrep -f "revenue_gateway")
    echo "  • Rural Gateway: PID $RURAL_PID"
fi

if pgrep -f "ollama" > /dev/null; then
    echo "  • Ollama AI: RUNNING"
fi

if pgrep -f "cloudflared" > /dev/null; then
    echo "  • Cloudflare Tunnel: RUNNING"
fi

echo ""

# SECTION 3: QUICK ACTIONS
echo "🚀 QUICK ACTIONS MENU"
echo "===================="
echo "1. Generate Emergency Cash (Urban)"
echo "2. Check Absa Account Status"
echo "3. Run Daily Cash Flow Report"
echo "4. Start Nightly Surge (21:00)"
echo "5. Manual Settlement to Absa"
echo "6. System Performance Check"
echo ""

read -p "Select action (1-6) or Enter for dashboard refresh: " CHOICE

case $CHOICE in
    1)
        echo "💵 LAUNCHING EMERGENCY CASH GENERATOR..."
        ~/humbu_community_nexus/emergency_cash.sh
        ;;
    2)
        echo "🏦 CHECKING ABSA ACCOUNT STATUS..."
        ~/humbu_community_nexus/check_absa.sh
        ;;
    3)
        echo "📊 GENERATING DAILY CASH FLOW REPORT..."
        ~/humbu_community_nexus/cash_dashboard.sh
        ;;
    4)
        echo "🏙️ STARTING NIGHTLY URBAN SURGE..."
        ~/humbu_community_nexus/auto_surge.sh
        ;;
    5)
        echo "💰 INITIATING MANUAL SETTLEMENT..."
        ~/humbu_community_nexus/dawn_settlement.sh
        ;;
    6)
        echo "🖥️ RUNNING SYSTEM PERFORMANCE CHECK..."
        echo "CPU Load: $(uptime | awk -F'load average:' '{print $2}')"
        echo "Memory: $(free -h | awk '/^Mem:/ {print $3"/"$2}')"
        echo "Disk: $(df -h / | awk 'NR==2 {print $3"/"$2 " ("$5")"}')"
        ;;
    *)
        echo "🔄 Refreshing dashboard..."
        sleep 2
        clear
        exec "$0"
        ;;
esac

echo ""
echo "======================================================"
echo "🏛️  END OF REPORT - CEO MURSHACK MUDAU APPROVED"
echo "======================================================"
