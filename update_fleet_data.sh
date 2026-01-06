#!/bin/bash
# 🚚 AUTO-UPDATE FLEET TELEMETRY DATA
while true; do
    TIMESTAMP=$(date '+%H:%M:%S')
    echo "$TIMESTAMP - Updating fleet telemetry data..."
    
    # Update the JSON file with new timestamps
    if [ -f ~/humbu_community_nexus/fleet_telemetry.json ]; then
        # Use sed to update timestamp
        sed -i "s/\"last_update\": \".*\"/\"last_update\": \"$(date -u '+%Y-%m-%dT%H:%M:%S.%3NZ')\"/" ~/humbu_community_nexus/fleet_telemetry.json
        sed -i "s/\"last_system_update\": \".*\"/\"last_system_update\": \"$(date '+%H:%M:%S')\"/" ~/humbu_community_nexus/fleet_telemetry.json
        
        # Occasionally update vehicle statuses (simulate movement)
        if [ $((RANDOM % 10)) -eq 0 ]; then
            STATUSES=("In Transit" "Unloading" "Loading" "Returning" "Route Optimizing")
            for i in {1..17}; do
                NEW_STATUS=${STATUSES[$RANDOM % ${#STATUSES[@]}]}
                sed -i "s/\"status\": \"[^\"]*\", \"location\": \".*\", \"temp\": \".*\", \"last_update\": \".*\"/\"status\": \"$NEW_STATUS\", \"location\": \"Gauteng Gateway\", \"temp\": \"$((20 + RANDOM % 15)).$((RANDOM % 10))°C\", \"last_update\": \"$(date '+%H:%M:%S')\"/" ~/humbu_community_nexus/fleet_telemetry.json
            done
        fi
        
        echo "$TIMESTAMP - Fleet data updated"
    fi
    
    sleep 30  # Update every 30 seconds
done
