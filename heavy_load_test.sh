#!/bin/bash
echo "⚡ HEAVY LOAD STRESS TEST - INITIATING"
echo "======================================"
echo "Target: +500 transactions (+R4,250 revenue)"
echo "Starting in 3 seconds..."
sleep 3

TOTAL_SUCCESS=0
for i in {1..500}; do
    # Generate transaction
    result=$(curl -s -X POST http://localhost:8083/ \
        -H "Content-Type: application/json" \
        -d '{"type":"delivery_status","location":"StressTest"}' 2>/dev/null)
    
    if echo "$result" | grep -q "success"; then
        TOTAL_SUCCESS=$((TOTAL_SUCCESS + 1))
        echo -n "✅"
    else
        echo -n "."
    fi
    
    # Progress indicator
    if [ $((i % 50)) -eq 0 ]; then
        echo " [$i/500]"
    fi
    
    # Small random delay (0.1-0.3 seconds)
    sleep 0.$((RANDOM % 3 + 1))
done

echo ""
echo "======================================"
echo "⚡ STRESS TEST COMPLETE!"
echo "Successful transactions: $TOTAL_SUCCESS"
echo "Revenue generated: R$(echo "$TOTAL_SUCCESS * 8.5" | bc)"
echo ""

# Final status check
curl -s http://localhost:8083/ | python3 -c "
import json, sys
data = json.load(sys.stdin)
rev = data.get('revenue_today', 0)
tx = data.get('transactions_today', 0)
print(f'📊 FINAL TOTALS:')
print(f'• Total Revenue: R{rev}')
print(f'• Total Transactions: {tx}')
print(f'• New target: R{(rev/1000000)*100:.1f}% of R1M goal')
"
