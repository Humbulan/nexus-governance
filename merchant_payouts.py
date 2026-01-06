#! /usr/bin/env python3
import sqlite3

db = sqlite3.connect('community_nexus.db')
cursor = db.cursor()

print("\n💰 PENDING MERCHANT SETTLEMENTS")
print("=" * 40)

# Join transactions with marketplace to find which merchant/village to pay
cursor.execute('''
    SELECT m.village, m.name, SUM(t.amount) 
    FROM transactions t
    JOIN marketplace m ON t.item_id = m.barcode
    WHERE t.status = 'SUCCESS'
    GROUP BY m.village, m.name
''')

payouts = cursor.fetchall()

if not payouts:
    print("No pending payouts.")
else:
    for village, item, amount in payouts:
        # We take a 1% platform fee to keep the USSD running
        fee = amount * 0.01
        net = amount - fee
        print(f"📍 {village}")
        print(f"   Item: {item}")
        print(f"   Total: R{amount:.2f}")
        print(f"   Fee (1%): R{fee:.2f}")
        print(f"   PAY MERCHANT: R{net:.2f}")
        print("-" * 20)

db.close()
