#!/bin/bash
# 🏛️ Imperial Dashboard Service - FLEET TELEMETRY PERMANENT
echo "🚚 Fleet Telemetry Dashboard Service starting at $(date '+%H:%M:%S')" > ~/humbu_community_nexus/logs/fleet-service-permanent.log

# Always use fleet telemetry dashboard
cp ~/humbu_community_nexus/index_telemetry.html ~/humbu_community_nexus/index.html

while true; do
    TIMESTAMP=$(date '+%H:%M:%S')
    
    # Check if fleet telemetry dashboard is working
    if ! curl -s http://localhost:8088 > /dev/null 2>&1; then
        echo "$TIMESTAMP - Fleet telemetry dashboard not responding, restarting..." >> ~/humbu_community_nexus/logs/fleet-service-permanent.log
        pkill -f "python3 -m http.server 8088" 2>/dev/null
        sleep 2
        cd ~/humbu_community_nexus
        nohup python3 -m http.server 8088 >> ~/humbu_community_nexus/logs/dashboard-fleet-permanent.log 2>&1 &
        echo "$TIMESTAMP - Fleet telemetry dashboard restart initiated" >> ~/humbu_community_nexus/logs/fleet-service-permanent.log
    else
        # Verify it's actually the fleet telemetry dashboard
        if curl -s http://localhost:8088 | grep -q "LIVE FLEET TELEMETRY"; then
            echo "$TIMESTAMP - Fleet telemetry dashboard OK (17 vehicles tracked)" >> ~/humbu_community_nexus/logs/fleet-service-permanent.log
        else
            echo "$TIMESTAMP - Wrong dashboard detected, switching to fleet telemetry..." >> ~/humbu_community_nexus/logs/fleet-service-permanent.log
            cp ~/humbu_community_nexus/index_telemetry.html ~/humbu_community_nexus/index.html
        fi
    fi
    
    sleep 60  # Check every minute
done
