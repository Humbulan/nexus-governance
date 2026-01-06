#!/usr/bin/env python3
"""
Daily status check for Humbu Community Nexus
"""

import sqlite3
from datetime import datetime, timedelta
import json
import os

def daily_status_check():
    print("📊 HUMBU COMMUNITY NEXUS - DAILY STATUS CHECK")
    print("=" * 50)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    db = sqlite3.connect('community_nexus.db')
    cursor = db.cursor()
    
    # Yesterday's date
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    # Get yesterday's transactions
    cursor.execute('''
    SELECT COUNT(*), SUM(amount) 
    FROM transactions 
    WHERE date(timestamp) = date('now', '-1 day')
    ''')
    yest_count, yest_total = cursor.fetchone()
    yest_total = yest_total or 0
    
    # Get today's transactions so far
    cursor.execute('''
    SELECT COUNT(*), SUM(amount) 
    FROM transactions 
    WHERE date(timestamp) = date('now')
    ''')
    today_count, today_total = cursor.fetchone()
    today_total = today_total or 0
    
    # Marketplace stats
    cursor.execute('SELECT COUNT(*) FROM marketplace')
    total_items = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(DISTINCT village) FROM marketplace')
    villages = cursor.fetchone()[0]
    
    # Recent transactions (last 5)
    cursor.execute('''
    SELECT timestamp, type, amount, status 
    FROM transactions 
    ORDER BY timestamp DESC 
    LIMIT 5
    ''')
    recent_tx = cursor.fetchall()
    
    db.close()
    
    # Print report
    print(f"\n💰 TRANSACTIONS:")
    print(f"   Yesterday ({yesterday}): {yest_count or 0} transactions, R{yest_total:.2f}")
    print(f"   Today (so far): {today_count or 0} transactions, R{today_total:.2f}")
    
    print(f"\n🏪 MARKETPLACE:")
    print(f"   Total Items: {total_items}")
    print(f"   Villages Covered: {villages}")
    
    if recent_tx:
        print(f"\n📋 RECENT TRANSACTIONS:")
        for ts, ttype, amount, status in recent_tx:
            status_icon = "✅" if status == 'SUCCESS' else "⏳"
            time_only = ts.split()[1] if ' ' in ts else ts
            print(f"   {time_only} - {ttype}: R{amount:.2f} {status_icon}")
    
    # Save to daily log
    log_entry = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'check_time': datetime.now().strftime('%H:%M:%S'),
        'yesterday_transactions': yest_count or 0,
        'yesterday_value': float(yest_total),
        'today_transactions': today_count or 0,
        'today_value': float(today_total),
        'total_items': total_items,
        'villages_covered': villages
    }
    
    # Append to daily log file
    log_file = 'logs/daily_status.json'
    os.makedirs('logs', exist_ok=True)
    
    # Read existing logs
    logs = []
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            try:
                logs = json.load(f)
            except:
                logs = []
    
    # Add new entry
    logs.append(log_entry)
    
    # Keep only last 30 days
    if len(logs) > 30:
        logs = logs[-30:]
    
    # Save
    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2)
    
    # Also save to text log
    with open('logs/daily_status.txt', 'a') as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - ")
        f.write(f"Yesterday: {yest_count or 0} tx (R{yest_total:.2f}), ")
        f.write(f"Today: {today_count or 0} tx (R{today_total:.2f})\n")
    
    print(f"\n📝 Status logged to: {log_file}")
    print(f"✅ Daily check complete")

if __name__ == "__main__":
    daily_status_check()
