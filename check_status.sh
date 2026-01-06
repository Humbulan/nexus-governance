#!/bin/bash
echo "🛡️ HUMBU IMPERIAL SYSTEM SENTINEL"
echo "----------------------------------"
PORTS=(8088 8089 11434 1808 1880 8086 8082 8083)
NAMES=("Main Portal" "Portal Mirror" "Llama AI" "Aviation" "Automation" "Fleet Hub" "Village API" "Industrial")

for i in "${!PORTS[@]}"; do
  (echo > /dev/tcp/127.0.0.1/${PORTS[$i]}) >/dev/null 2>&1
  if [ $? -eq 0 ]; then
    echo -e "✅ [${PORTS[$i]}] ${NAMES[$i]}: ONLINE"
  else
    echo -e "❌ [${PORTS[$i]}] ${NAMES[$i]}: OFFLINE"
  fi
done
echo "----------------------------------"
echo "Wake-Lock Status: $(termux-wake-lock -s 2>/dev/null || echo "Active")"
