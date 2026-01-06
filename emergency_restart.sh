#!/bin/bash
echo "🚨 EMERGENCY API RESTART - 2 HOUR COUNTDOWN"
echo "=========================================="
echo ""

# Calculate end time (2 hours from now)
end_time=$(date -d "+2 hours" +%s)
current_time=$(date +%s)
seconds_left=$((end_time - current_time))

echo "⏰ TIME LEFT: $((seconds_left / 3600))h $(((seconds_left % 3600) / 60))m"
echo "🎯 TARGET: Maximum API uptime and performance"
echo ""

# Kill all existing API processes
echo "1. Stopping all API processes..."
pkill -f "python.*(8080|8083|8086|9090)" 2>/dev/null
pkill -f "node.*1880" 2>/dev/null
pkill -f "ollama" 2>/dev/null
sleep 2

echo "2. Starting high-priority APIs..."

# Start Health API (Highest priority)
echo "   🔼 Starting Health API (port 9090)..."
nohup python3 ~/humbu_community_nexus/health_api.py > ~/logs/health_api.log 2>&1 &
sleep 3

# Start Business API
echo "   🔼 Starting Business API (port 8080)..."
nohup python3 ~/humbu_community_nexus/community_web.py > ~/logs/business_api.log 2>&1 &
sleep 3

# Start Government API
echo "   🔼 Starting Government API (port 8083)..."
nohup python3 ~/humbu_community_nexus/government_api.py > ~/logs/government_api.log 2>&1 &
sleep 3

# Start Revenue Bridge
echo "   🔼 Starting Revenue Bridge (port 8086)..."
nohup python3 ~/humbu_community_nexus/revenue_bridge.py > ~/logs/revenue_bridge.log 2>&1 &
sleep 3

echo ""
echo "3. Verifying all APIs..."
sleep 5

# Verify all ports
ports=(9090 8080 8083 8086)
all_up=true

for port in "${ports[@]}"; do
    if nc -z localhost $port 2>/dev/null; then
        echo "   ✅ Port $port: UP"
    else
        echo "   ❌ Port $port: DOWN"
        all_up=false
    fi
done

echo ""
if $all_up; then
    echo "🎉 ALL APIS RUNNING!"
    echo "📊 Health check: curl http://localhost:9090/health"
    echo "📈 Metrics: curl http://localhost:9090/metrics"
else
    echo "⚠️  Some APIs failed. Check logs in ~/logs/"
fi

echo ""
echo "4. Starting aggressive monitoring..."
# Create monitoring loop that restarts failed APIs
cat << 'MONITOR' > ~/humbu_community_nexus/aggressive_monitor.sh
#!/bin/bash
echo "🔴 AGGRESSIVE MONITOR STARTED - 2 HOUR RACE"
echo "Target: Keep all APIs up until $(date -d "+2 hours" "+%H:%M")"

while [ $(date +%s) -lt $end_time ]; do
    for port in 9090 8080 8083 8086; do
        if ! nc -z localhost $port 2>/dev/null; then
            echo "[$(date '+%H:%M:%S')] ❌ Port $port down - RESTARTING"
            case $port in
                9090) nohup python3 ~/humbu_community_nexus/health_api.py > ~/logs/health_api_restart.log 2>&1 & ;;
                8080) nohup python3 ~/humbu_community_nexus/community_web.py > ~/logs/business_api_restart.log 2>&1 & ;;
                8083) nohup python3 ~/humbu_community_nexus/government_api.py > ~/logs/government_api_restart.log 2>&1 & ;;
                8086) nohup python3 ~/humbu_community_nexus/revenue_bridge.py > ~/logs/revenue_bridge_restart.log 2>&1 & ;;
            esac
            sleep 3
        fi
    done
    
    # Show status every 30 seconds
    if [ $(( $(date +%s) % 30 )) -eq 0 ]; then
        echo -n "[$(date '+%H:%M:%S')] "
        for port in 9090 8080 8083 8086; do
            if nc -z localhost $port 2>/dev/null; then
                echo -n "✅$port "
            else
                echo -n "❌$port "
            fi
        done
        time_left=$((end_time - $(date +%s)))
        echo "- Time left: $((time_left / 60))m"
    fi
    
    sleep 5
done

echo "⏰ TIME'S UP! 2-HOUR RACE COMPLETE"
echo "🎯 Target reached at $(date)"
MONITOR

chmod +x ~/humbu_community_nexus/aggressive_monitor.sh
nohup ~/humbu_community_nexus/aggressive_monitor.sh > ~/logs/aggressive_monitor.log 2>&1 &

echo ""
echo "🚀 AGGRESSIVE MONITOR STARTED IN BACKGROUND"
echo "📝 Logs: ~/logs/aggressive_monitor.log"
echo "⏰ Will auto-restart any failed API for next 2 hours"
echo ""
echo "🎯 TARGET LOCKED: Maximum uptime for next 2 hours"
