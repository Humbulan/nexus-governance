#!/bin/bash
echo "💰 HUMBU REVENUE GENERATOR v2"
echo "============================="
echo "1. Generate 1 transaction"
echo "2. Generate 10 transactions (BULK)"
echo "3. Generate 100 transactions (STRESS TEST)"
echo "4. Continuous generation"
echo "5. Check gateway status"
echo "6. View revenue dashboard"
echo ""
read -p "Choice: " choice

get_revenue() {
    response=$(curl -s -X POST http://localhost:8083/ \
        -H "Content-Type: application/json" \
        -d "$1")
    echo "$response" | grep -o '"revenue_generated":[0-9.]*' | cut -d: -f2
}

case $choice in
    1)
        echo "Generating 1 transaction..."
        curl -X POST http://localhost:8083/ \
            -H "Content-Type: application/json" \
            -d '{"type":"delivery_status","location":"Maniini Hub"}' \
            2>/dev/null | python3 -m json.tool
        ;;
    2)
        echo "Generating 10 transactions..."
        total=0
        for i in {1..10}; do
            types=("delivery_status" "gps_tracking" "soil_moisture" "livestock_health" "weather_data" "crop_health")
            type=${types[$RANDOM % ${#types[@]}]}
            data="{\"type\":\"$type\",\"location\":\"Village $i\"}"
            revenue=$(get_revenue "$data")
            if [ -n "$revenue" ]; then
                total=$(echo "$total + $revenue" | bc)
                echo "TX $i: $type → R$revenue"
            else
                echo "TX $i: $type → FAILED"
            fi
            sleep 0.3
        done
        echo "💰 TOTAL: R$total"
        ;;
    3)
        echo "Generating 100 transactions (STRESS TEST)..."
        total=0
        success=0
        for i in {1..100}; do
            types=("delivery_status" "gps_tracking" "soil_moisture" "livestock_health" "weather_data" "crop_health")
            type=${types[$RANDOM % ${#types[@]}]}
            data="{\"type\":\"$type\",\"location\":\"Bulk Test $i\"}"
            revenue=$(get_revenue "$data")
            if [ -n "$revenue" ]; then
                total=$(echo "$total + $revenue" | bc)
                success=$((success + 1))
                if [ $((i % 20)) -eq 0 ]; then
                    echo "Progress: $i/100 (R$total)"
                fi
            fi
            sleep 0.1
        done
        echo "✅ COMPLETED: $success successful transactions"
        echo "💰 TOTAL REVENUE: R$total"
        echo "📊 AVERAGE PER TX: R$(echo "scale=2; $total / $success" | bc)"
        ;;
    4)
        echo "Continuous generation (Ctrl+C to stop)..."
        count=1
        total=0
        while true; do
            types=("delivery_status" "gps_tracking" "soil_moisture" "livestock_health" "weather_data" "crop_health")
            type=${types[$RANDOM % ${#types[@]}]}
            data="{\"type\":\"$type\",\"location\":\"Live $count\"}"
            revenue=$(get_revenue "$data")
            if [ -n "$revenue" ]; then
                total=$(echo "$total + $revenue" | bc)
                echo "TX $count: $type → R$revenue (Total: R$total)"
            fi
            count=$((count + 1))
            sleep 1
        done
        ;;
    5)
        echo "Gateway status:"
        curl -s http://localhost:8083/ | python3 -m json.tool 2>/dev/null || echo "Gateway not responding"
        ;;
    6)
        echo "Revenue Dashboard Loading..."
        echo "============================"
        # Get current status
        status=$(curl -s http://localhost:8083/)
        tx_today=$(echo "$status" | grep -o '"transactions_today":[0-9]*' | cut -d: -f2)
        rev_today=$(echo "$status" | grep -o '"revenue_today":[0-9]*' | cut -d: -f2)
        
        echo "📊 TODAY'S STATS:"
        echo "• Transactions: $tx_today"
        echo "• Revenue: R$rev_today"
        echo "• Avg/TX: R$(echo "scale=2; $rev_today / $tx_today" | bc)"
        echo ""
        echo "📈 PROJECTIONS:"
        echo "• Daily: R$(echo "$rev_today * 1.2" | bc)"
        echo "• Weekly: R$(echo "$rev_today * 7" | bc)"
        echo "• Monthly: R$(echo "$rev_today * 30" | bc)"
        echo ""
        echo "🚀 TARGET PROGRESS:"
        monthly=$(echo "$rev_today * 30" | bc)
        progress=$(echo "scale=1; ($monthly / 1000000) * 100" | bc)
        echo "• Current: R$monthly/month"
        echo "• Target: R1,000,000/month"
        echo "• Progress: $progress%"
        ;;
    *)
        echo "Invalid choice"
        ;;
esac
