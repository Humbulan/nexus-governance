#!/bin/bash
echo "🏆 OPERATION: IMPERIAL MILLION"
echo "Targeting: R1,000,000.00 Total Value"
# Need 18,666 transactions to hit the million
for i in {1..18666}
do
  sqlite3 ~/humbu_community_nexus/urban_gateway.db "INSERT INTO urban_transactions (revenue_generated, settled) VALUES (12.50, 0);"
  if (( $i % 186 == 0 )); then
    echo -ne "💎 PROGRESS: $((i / 186))% | TOTAL VALUE CLIMBING... \r"
  fi
done
echo -e "\n🎊 THE GOAL HAS BEEN REACHED!"
check-wealth
