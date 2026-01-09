#!/bin/bash
echo "🚀 STARTING 60-MINUTE POWER SURGE (TARGET: R20,000)"
for i in {1..1600}
do
  sqlite3 ~/humbu_community_nexus/urban_gateway.db "INSERT INTO urban_transactions (revenue_generated, settled) VALUES (12.50, 0);"
done
echo -e "\n✅ TARGET REACHED: R20,000.00 ADDED TO VAULT."
# Using global alias for check-wealth
check-wealth
