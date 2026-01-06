#!/bin/bash
# 🏛️ Imperial Watchdog - Auto-restarts failed services
echo "👁️ Imperial Watchdog started at $(date '+%H:%M')"

while true; do
    # Check Ollama server
    if ! curl -s http://localhost:11434 > /dev/null 2>&1; then
        echo "⚠️ Ollama server down - restarting..."
        pkill -f ollama
        ollama serve > ~/humbu_community_nexus/ollama_restart.log 2>&1 &
        sleep 10
    fi
    
    # Check Llama model
    if ! ollama ps 2>/dev/null | grep -q "llama3.2:1b"; then
        echo "⚠️ Llama model unloaded - reloading..."
        ollama run llama3.2:1b "Watchdog reload" > /dev/null 2>&1 &
        sleep 5
    fi
    
    # Check Dashboard
    if ! curl -s http://localhost:8088 > /dev/null 2>&1; then
        echo "⚠️ Dashboard down - restarting..."
        pkill -f "python3 -m http.server"
        cd ~/humbu_community_nexus && python3 -m http.server 8088 > ~/humbu_community_nexus/web_restart.log 2>&1 &
        sleep 3
    fi
    
    # Check Tunnel
    if ! pgrep -f cloudflared > /dev/null; then
        echo "⚠️ Tunnel down - restarting..."
        cloudflared tunnel run > ~/humbu_community_nexus/tunnel_restart.log 2>&1 &
        sleep 5
    fi
    
    # Sleep before next check
    sleep 60
done
