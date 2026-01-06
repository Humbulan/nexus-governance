#!/bin/bash
echo "🏁 HUMBU API 2-HOUR MARATHON STARTING"
echo "====================================="
echo "Start time: $(date)"
echo "End target: $(date -d "+2 hours" "+%H:%M")"
echo "Goal: Maximum API uptime and performance"
echo ""

# Step 1: Run API booster
echo "1. 🚀 BOOSTING API PERFORMANCE..."
python3 ~/humbu_community_nexus/api_booster.py

# Step 2: Emergency restart
echo ""
echo "2. 🔄 EMERGENCY RESTART..."
~/humbu_community_nexus/emergency_restart.sh

# Step 3: Start load test (optional)
echo ""
echo "3. 📊 STARTING LOAD TEST (Optional)..."
read -p "Run load test? (y/n): " choice
if [[ $choice == "y" || $choice == "Y" ]]; then
    echo "   Starting load test in background..."
    nohup python3 ~/humbu_community_nexus/load_test.py 3600 > ~/logs/load_test.log 2>&1 &
    echo "   ✅ Load test running (1 hour)"
fi

# Step 4: Show monitoring
echo ""
echo "4. 📈 REAL-TIME MONITORING..."
echo "   Run these commands in separate terminals:"
echo ""
echo "   Terminal 1: watch -n 5 'curl -s http://localhost:9090/health | python3 -m json.tool'"
echo "   Terminal 2: watch -n 10 'curl -s http://localhost:9090/metrics | python3 -m json.tool'"
echo "   Terminal 3: ./api_monitor.sh"
echo ""
echo "   Or use the aggressive monitor already running in background"
echo "   Check logs: tail -f ~/logs/aggressive_monitor.log"

# Step 5: Final countdown
echo ""
echo "5. ⏰ FINAL COUNTDOWN STARTING..."
echo "   Time remaining: 2 hours"
echo "   Target: Keep all APIs up until $(date -d "+2 hours" "+%H:%M")"
echo ""
echo "🎯 SUCCESS METRICS:"
echo "   • All 4 APIs (9090, 8080, 8083, 8086) stay up"
echo "   • Response time < 500ms"
echo "   • Success rate > 95%"
echo "   • Handle minimum 1000 requests/hour"
echo ""
echo "🚀 EXECUTION STARTED: $(date)"
echo "🎯 TARGET END TIME: $(date -d "+2 hours" "+%H:%M")"
