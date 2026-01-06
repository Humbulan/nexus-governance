#! /usr/bin/env python3
#!/usr/bin/env python3
import sqlite3
import os
import time
import csv
from datetime import datetime

# --- CONFIGURATION ---
MY_PHONE_NUMBER = "27794658481"
PLATFORM_NAME = "HUMBU NEXUS"
CHAMPION_BONUS_RATE = 0.02  # 2% bonus for the Village Champion
# ---------------------

def get_weekly_summary():
    db = sqlite3.connect('community_nexus.db')
    cursor = db.cursor()

    # Core Stats
    cursor.execute('''
        SELECT COUNT(*), SUM(amount), SUM(amount) * 0.05, SUM(amount) * 0.93 
        FROM transactions 
        WHERE date(timestamp) >= date('now', 'weekday 0', '-7 days') 
        AND status = 'SUCCESS'
    ''')
    res = cursor.fetchone()
    
    # Champion Bonus Calculation (2% of total sales)
    total_sales = res[1] or 0
    champ_bonus = total_sales * CHAMPION_BONUS_RATE

    # Get Top Village
    cursor.execute('''
        SELECT m.village, COUNT(*) as sales 
        FROM transactions t 
        JOIN marketplace m ON t.type LIKE '%' || m.name || '%' 
        WHERE date(t.timestamp) >= date('now', 'weekday 0', '-7 days') 
        GROUP BY m.village ORDER BY sales DESC LIMIT 1
    ''')
    top = cursor.fetchone()
    top_v = top[0] if top else "None"
    
    db.close()
    return {
        'sales': total_sales, 'tx': res[0] or 0, 'fee': res[2] or 0,
        'payouts': res[3] or 0, 'bonus': champ_bonus, 'village': top_v
    }

def send_payout_sms():
    data = get_weekly_summary()
    msg = f"[{PLATFORM_NAME}] Weekly Report\n" \
          f"💰 Sales: R{data['sales']:.2f}\n" \
          f"🏆 Top Village: {data['village']}\n" \
          f"👨‍🌾 Seller Pay: R{data['payouts']:.2f}\n" \
          f"🏅 Champ Bonus: R{data['bonus']:.2f}\n" \
          f"💼 Nexus Fee: R{data['fee']:.2f}"

    print(f"📋 SMS PREVIEW:\n{msg}\n" + "="*40)
    os.system(f'termux-sms-send -n {MY_PHONE_NUMBER} "{msg}"')
    print("✅ Payout SMS with Champion Bonus Sent!")

if __name__ == "__main__":
    send_payout_sms()
