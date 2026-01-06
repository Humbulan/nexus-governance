#!/bin/bash
echo "💰 SIMPLE REVENUE GENERATOR"
echo "==========================="
echo "1. Make 1 transaction"
echo "2. Make 5 transactions"
echo "3. Check gateway"
echo ""
read -p "Choose: " choice

case $choice in
    1)
        echo "Making 1 transaction..."
        curl -X POST http://localhost:8083/ \
          -H "Content-Type: application/json" \
          -d '{"type":"delivery_status","location":"Quick"}' | \
          python3 -c "import json,sys; d=json.load(sys.stdin); print(f'✅ {d[\"government_id\"]}: R{d[\"revenue_generated\"]}')"
        ;;
    2)
        echo "Making 5 transactions..."
        total=0
        for i in {1..5}; do
            types=("delivery_status" "gps_tracking" "soil_moisture" "livestock_health" "weather_data")
            type=${types[$RANDOM % ${#types[@]}]}
            result=$(curl -s -X POST http://localhost:8083/ \
              -H "Content-Type: application/json" \
              -d "{\"type\":\"$type\",\"location\":\"Batch $i\"}")
            revenue=$(echo "$result" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('revenue_generated', 0))")
            total=$(echo "$total + $revenue" | bc)
            echo "TX $i: $type → R$revenue"
            sleep 0.5
        done
        echo "💰 TOTAL: R$total"
        ;;
    3)
        echo "Gateway status:"
        curl -s http://localhost:8083/ | python3 -m json.tool
        ;;
    *)
        echo "Invalid choice"
        ;;
esac
