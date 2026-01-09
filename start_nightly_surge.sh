#!/bin/bash
echo "🏙️ STARTING NIGHTLY URBAN SURGE"
echo "==============================="
echo "Time: $(date)"
echo ""

# Check if gateway is running
if ! curl -s http://localhost:8084/ > /dev/null; then
    echo "❌ Urban Gateway is not running"
    echo "Starting gateway..."
    nohup python3 /data/data/com.termux/files/home/humbu_community_nexus/urban_gateway_simple.py > /data/data/com.termux/files/home/humbu_community_nexus/gateway.log 2>&1 &
    sleep 3
fi

# Start the surge
echo "🚀 Launching Urban Nightly Surge..."
echo "Operational Window: 21:00 - 04:00"
echo "Revenue Target: R700,000"
echo ""

# Run surge for specified duration (in minutes)
DURATION_MINUTES=${1:-420}  # Default 7 hours
echo "Running surge for $DURATION_MINUTES minutes (Ctrl+C to stop early)"
echo ""

timeout ${DURATION_MINUTES}m python3 /data/data/com.termux/files/home/humbu_community_nexus/urban_nightly_surge.py

echo ""
echo "🏁 Surge completed at $(date)"
