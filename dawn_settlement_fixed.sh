#!/bin/bash
echo "🏛️ HUMBUSINESS DAWN SETTLEMENT - FIXED"
echo "==============================="
echo "Time: $(date)"
echo "Business: HUMBU AI PLATFORM"
echo "ShapID: 21000178769"
echo "Bank: Absa"
echo ""

# Get REAL transaction data
DB_PATH=~/humbu_community_nexus/urban_gateway.db

# Get total transactions AND total amount (FIXED!)
UNSETTLED_DATA=$(sqlite3 "$DB_PATH" "SELECT COUNT(*), COALESCE(SUM(revenue_generated), 0) FROM urban_transactions WHERE settled = 0" 2>/dev/null || echo "0|0")
TOTAL_TX=$(echo "$UNSETTLED_DATA" | cut -d'|' -f1)
TOTAL_AMOUNT=$(echo "$UNSETTLED_DATA" | cut -d'|' -f2)

# Get last settlement date
LAST_SETTLEMENT=$(sqlite3 "$DB_PATH" "SELECT MAX(settled_at) FROM settlement_batch WHERE status = 'COMPLETED'" 2>/dev/null || echo "1970-01-01")

if [ "$TOTAL_TX" -eq 0 ] || [ "$(echo "$TOTAL_AMOUNT == 0" | bc -l)" -eq 1 ]; then
    echo "✅ No new transactions to settle"
    echo "   Last settlement: $LAST_SETTLEMENT"
    exit 0
fi

echo "📊 SETTLEMENT BATCH READY"
echo "• Transactions: $TOTAL_TX"
echo "• Amount: R$TOTAL_AMOUNT"
echo "• Target: HUMBU AI PLATFORM (ShapID: 21000178769)"
echo "• Bank: Absa"
echo ""

# Create settlement batch
BATCH_ID="HUMBU-$(date +%Y%m%d-%H%M%S)"
sqlite3 "$DB_PATH" << EOF
INSERT INTO settlement_batch
(batch_id, total_transactions, total_amount, settlement_target, created_at, status)
VALUES ('$BATCH_ID', $TOTAL_TX, $TOTAL_AMOUNT, '21000178769', '$(date -Iseconds)', 'PROCESSING');
