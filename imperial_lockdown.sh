#!/bin/bash
echo "🔒 IMPERIAL LOCKDOWN PROTOCOL ACTIVATED"
echo "========================================"
echo "🛡️ Securing all critical ports..."

# Kill all conflicting processes
pkill -f "python.*http.server"
pkill -f "community_web"
pkill -f "node-red"

# Start Executive Dashboard on guaranteed port
for port in {8088..8095}; do
    if ! nc -z localhost $port 2>/dev/null; then
        echo "🎯 Locking Executive Dashboard to port $port"
        cd ~/humbu_community_nexus
        nohup python3 -m http.server $port --bind 0.0.0.0 > ~/logs/dashboard_lockdown.log 2>&1 &
        sleep 2
        if curl -s http://localhost:$port > /dev/null; then
            echo "✅ Dashboard secured on port $port"
            DASH_PORT=$port
            break
        fi
    fi
done

# Restart Node-RED
echo "🤖 Restarting Automation Engine..."
nohup node-red > ~/logs/automation_lockdown.log 2>&1 &
sleep 3

# Update Cloudflare Tunnel
echo "🌐 Reconstituting Public Access..."
pkill -f cloudflared
sleep 2
nohup cloudflared tunnel run --url http://localhost:$DASH_PORT humbu-imperial > ~/logs/tunnel_lockdown.log 2>&1 &
sleep 3

# Verify everything
echo ""
echo "🔍 FINAL VERIFICATION:"
echo "---------------------"
echo "Dashboard: $(curl -s --max-time 3 http://localhost:$DASH_PORT >/dev/null && echo '✅' || echo '❌') http://localhost:$DASH_PORT"
echo "Public: $(curl -s --max-time 3 monitor.humbu.store >/dev/null && echo '✅' || echo '❌') monitor.humbu.store"
echo "Automation: $(nc -z localhost 1880 2>/dev/null && echo '✅' || echo '❌')"
echo "Sage AI: $(pgrep -f ollama >/dev/null && echo '✅' || echo '❌')"

echo ""
echo "📊 FINANCIAL COMMAND CENTER:"
echo "http://localhost:$DASH_PORT/index_financial_command.html"
echo ""
echo "🔒 LOCKDOWN COMPLETE - IDC PRESENTATION READY"
