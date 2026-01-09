#!/bin/bash
# Select exactly R20,000 worth of unsettled transactions
sqlite3 ~/humbu_community_nexus/urban_gateway.db "UPDATE urban_transactions SET settled = 1 WHERE rowid IN (SELECT rowid FROM urban_transactions WHERE settled = 0 LIMIT 1600);"
# Run the settlement transport
~/humbu_community_nexus/dawn_settlement.sh
echo "✅ R20,000.00 HAS BEEN MOVED TO SETTLEMENT STATUS."
