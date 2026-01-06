import sqlite3
import time
import os
from datetime import datetime

def get_tx_count():
    try:
        db = sqlite3.connect('community_nexus.db')
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*), SUM(amount), MAX(timestamp) FROM transactions")
        count, total, last_time = cursor.fetchone()
        db.close()
        return count, total or 0, last_time
    except Exception as e:
        return 0, 0, None

# Initialize
last_count, _, _ = get_tx_count()

print("\033[95m" + "="*50)
print("📡 NEXUS TRANSACTION WATCHDOG ACTIVE")
print(f"Current Status: {last_count} Transactions | Monitoring for # {last_count + 1}...")
print("="*50 + "\033[0m")

try:
    while True:
        current_count, total_val, last_ts = get_tx_count()
        
        if current_count > last_count:
            # ALERT! New Transaction detected
            os.system('termux-vibrate -d 500') # Vibrates phone if Termux:API is installed
            
            print("\n" + "⭐" * 20)
            print(f"\033[92m🚀 NEW TRANSACTION DETECTED at {datetime.now().strftime('%H:%M:%S')}!")
            print(f"💰 New Platform Total: R{total_val:.2f}")
            print(f"📈 Transaction # {current_count} just cleared.")
            print(f"🕒 Timestamp: {last_ts}")
            print("⭐" * 20 + "\033[0m\n")
            
            last_count = current_count
            
        time.sleep(5) # Poll every 5 seconds
except KeyboardInterrupt:
    print("\n🛑 Watchdog standing down.")
