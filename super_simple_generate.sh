#!/bin/bash
echo "💸 HUMBU REVENUE - PRESS ENTER TO GENERATE R8.50"
echo "================================================"

while true; do
    read -p "Press Enter to generate revenue (or 'q' to quit): " input
    
    if [ "$input" = "q" ]; then
        echo "Goodbye! Total today:"
        curl -s http://localhost:8083/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'💰 R{d[\"revenue_today\"]} today from {d[\"transactions_today\"]} transactions')"
        break
    fi
    
    echo "Generating R8.50..."
    result=$(curl -s -X POST http://localhost:8083/ \
        -H "Content-Type: application/json" \
        -d '{"type":"delivery_status","location":"Auto"}')
    
    if echo "$result" | grep -q "success"; then
        echo "✅ SUCCESS: R8.50 added!"
    else
        echo "❌ FAILED: Check gateway"
    fi
    
    echo "---"
done
