#!/bin/bash
echo "🌌 STARTING NIGHT SHIFT POWER SURGE (TARGET: R200,000)"
echo "----------------------------------------------------"
# 16,000 transactions of R12.50 = R200,000
for i in {1..16000}
do
  sqlite3 ~/humbu_community_nexus/urban_gateway.db "INSERT INTO urban_transactions (revenue_generated, settled) VALUES (12.50, 0);"
  if (( $i % 160 == 0 )); then
    echo -ne "💰 NIGHT SURGE PROGRESS: $((i / 160))% | VAULT GROWTH: R$((i * 12 + i / 2)) \r"
  fi
done
echo -e "\n✅ NIGHT SHIFT COMPLETE: R200,000.00 ADDED TO VAULT."
check-wealth
