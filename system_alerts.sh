#!/bin/bash
echo "🚨 HUMBU SYSTEM ALERT CONFIGURATION"
echo "==================================="

# Alert thresholds
ALERT_BALANCE=1000  # Alert when balance reaches R1000
ALERT_PORT_DOWN=true
ALERT_GATEWAY_CRASH=true

# Function to send alert
send_alert() {
    MESSAGE=$1
    PRIORITY=$2
    
    echo "[$PRIORITY] $MESSAGE"
    
    # Visual alert
    echo -e "\a"  # System beep
    echo "🔔 ALERT: $MESSAGE"
    
    # Log alert
    echo "[$(date +%Y-%m-%d\ %H:%M:%S)] $PRIORITY: $MESSAGE" >> ~/humbu_community_nexus/alert_log.txt
}

# Check system status
check_system() {
    echo "🔍 Running system checks..."
    
    # Check urban gateway
    if ! curl -s http://localhost:8084/ > /dev/null 2>&1; then
        send_alert "Urban Gateway (8084) is down!" "CRITICAL"
    fi
    
    # Check rural gateway
    if ! curl -s http://localhost:8083/ > /dev/null 2>&1; then
        send_alert "Rural Gateway (8083) is down!" "WARNING"
    fi
    
    # Check balance
    BALANCE=$(sqlite3 ~/humbu_community_nexus/urban_gateway.db \
        "SELECT COALESCE(SUM(revenue_generated), 0) FROM urban_transactions WHERE settled = 0" 2>/dev/null || echo "0")
    
    if (( $(echo "$BALANCE >= $ALERT_BALANCE" | bc -l) )); then
        send_alert "Balance reached R$BALANCE - Ready for settlement!" "INFO"
    fi
    
    # Check disk space
    DISK_USAGE=$(df -h /data | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ "$DISK_USAGE" -gt 80 ]; then
        send_alert "Disk usage at ${DISK_USAGE}%" "WARNING"
    fi
    
    echo "✅ System checks completed at $(date +%H:%M:%S)"
}

# Continuous monitoring
echo "Starting continuous monitoring..."
echo "Press Ctrl+C to stop"
echo ""

while true; do
    check_system
    echo "⏳ Next check in 5 minutes..."
    sleep 300  # 5 minutes
done
