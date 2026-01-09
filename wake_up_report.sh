#!/bin/bash
REPORT_FILE=~/daily_summary_$(date +%Y%m%d).txt
echo "🌅 HUMBU MORNING CEO BRIEFING" > $REPORT_FILE
echo "==============================" >> $REPORT_FILE
echo "Date: $(date)" >> $REPORT_FILE
echo "" >> $REPORT_FILE
echo "💰 OVERNIGHT PERFORMANCE:" >> $REPORT_FILE
sqlite3 ~/humbu_community_nexus/urban_gateway.db "SELECT 'Total Generated: R' || SUM(revenue_generated) FROM urban_transactions WHERE DATE(timestamp) = DATE('now');" >> $REPORT_FILE
echo "" >> $REPORT_FILE
echo "🏦 SETTLEMENT STATUS:" >> $REPORT_FILE
sqlite3 ~/humbu_community_nexus/urban_gateway.db "SELECT 'Last Batch: ' || batch_id || ' | Amount: R' || total_amount FROM settlement_batch ORDER BY settled_at DESC LIMIT 1;" >> $REPORT_FILE
echo "" >> $REPORT_FILE
echo "🚀 NEXT STEP: Check Absa App for the overnight deposit." >> $REPORT_FILE
cat $REPORT_FILE
