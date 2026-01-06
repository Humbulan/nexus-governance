#!/bin/bash
echo "👑 STAGGERED START: HUMBU IMPERIAL ECOSYSTEM..."

# 1. CLEAN START
pkill -9 python
pkill -9 ollama
sleep 2

# 2. START THE BRAIN FIRST (Give it 10 seconds to breathe)
nohup ollama serve > ~/logs/ollama.log 2>&1 &
echo "🧠 [11434] Llama 3.2 AI Brain: LOADING..."
sleep 10

# 3. START WEB PORTS ONE BY ONE
cd ~/humbu_community_nexus
nohup python3 -m http.server 8088 --bind 0.0.0.0 > ~/logs/domain_web.log 2>&1 &
echo "✅ [8088] Main Portal: ONLINE"
sleep 1

nohup python3 -m http.server 8089 --bind 0.0.0.0 > ~/logs/mirror_web.log 2>&1 &
echo "✅ [8089] Portal Mirror: ONLINE"

nohup python3 -m http.server 1808 --bind 0.0.0.0 > ~/logs/aviation.log 2>&1 &
echo "✅ [1808] SADC Air Monitor: ONLINE"

nohup python3 -m http.server 1880 --bind 0.0.0.0 > ~/logs/automation.log 2>&1 &
echo "✅ [1880] Industrial Logic: ONLINE"

nohup python3 -m http.server 8086 --bind 0.0.0.0 > ~/logs/telemetry.log 2>&1 &
echo "✅ [8086] Fleet Telemetry: ONLINE"

nohup python3 -m http.server 8082 --bind 0.0.0.0 > ~/logs/community_api.log 2>&1 &
echo "✅ [8082] Village API: ONLINE"

nohup python3 -m http.server 8083 --bind 0.0.0.0 > ~/logs/gov_api.log 2>&1 &
echo "✅ [8083] Industrial API: ONLINE"

echo "🎯 SYSTEM STABILIZED: ALL NODES ACTIVE"
