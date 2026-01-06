#!/bin/bash
echo "🏛️ IMPERIAL GRID SENTINEL ACTIVE..."
while true; do
    NODES=$(ls ~/humbu_community_nexus/nodes/node_*.active 2>/dev/null | wc -l)
    TUNNELS=$(ls ~/.cloudflared/*.json 2>/dev/null | wc -l)
    
    if [ $NODES -lt 20 ] || [ $TUNNELS -lt 8 ]; then
        echo -e "\a" # System Bell
        echo "⚠️ ALERT: GRID INSTABILITY DETECTED"
        echo "Nodes: $NODES/20 | Tunnels: $TUNNELS/8"
    fi
    sleep 300 # Checks every 5 minutes
done
