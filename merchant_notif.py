#! /usr/bin/env python3
import sqlite3

def get_latest_sale():
    db = sqlite3.connect('community_nexus.db')
    cursor = db.cursor()
    cursor.execute('''
        SELECT t.timestamp, t.amount, m.name, m.village 
        FROM transactions t 
        JOIN marketplace m ON t.item_id = m.barcode 
        WHERE t.status = 'SUCCESS' 
        ORDER BY t.timestamp DESC LIMIT 1
    ''')
    result = cursor.fetchone()
    db.close()
    return result

sale = get_latest_sale()
if sale:
    ts, amt, item, village = sale
    print("\n📩 DRAFT SMS FOR MERCHANT:")
    print("-" * 30)
    print(f"Humbu Nexus: PAID R{amt:.2f} for {item} in {village}.")
    print(f"Time: {ts}")
    print("Please release goods to customer. ✅")
    print("-" * 30)
else:
    print("No transactions found yet.")
