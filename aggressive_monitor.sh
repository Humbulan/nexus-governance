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
