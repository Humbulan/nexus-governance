#!/bin/bash
echo "📊 HUMBU API REAL-TIME MONITOR"
echo "==============================="

while true; do
    clear
    echo "🕐 $(date '+%H:%M:%S') - API STATUS"
    echo "--------------------------------"
    
    # Check each port
    for port in 8080 8083 8086; do
        if timeout 1 bash -c "echo > /dev/tcp/localhost/$port" 2>/dev/null; then
            echo "✅ Port $port: ACTIVE"
            
            # Get response time
            start=$(date +%s%N)
            curl -s http://localhost:$port/health > /dev/null 2>&1
            end=$(date +%s%N)
            time_ms=$(( (end - start) / 1000000 ))
            echo "   Response time: ${time_ms}ms"
            
            # Get connection count
            conn=$(netstat -an | grep :$port | grep ESTABLISHED | wc -l)
            echo "   Active connections: $conn"
        else
            echo "❌ Port $port: DOWN"
        fi
        echo
    done
    
    # Show system resources
    echo "💻 SYSTEM RESOURCES:"
    echo "CPU: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}')%"
    echo "RAM: $(free -m | awk 'NR==2{printf "%.1f%%", $3*100/$2}')"
    echo "DISK: $(df -h / | awk 'NR==2{print $5}')"
    
    echo
    echo "📈 Last 5 transactions:"
    sqlite3 ~/humbu_community_nexus/community_nexus.db "SELECT strftime('%H:%M', timestamp), amount FROM transactions ORDER BY timestamp DESC LIMIT 5;" 2>/dev/null || echo "No transactions"
    
    sleep 5
done
