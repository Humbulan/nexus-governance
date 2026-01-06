import sqlite3
from datetime import datetime, timedelta

def generate_daily_report():
    db = sqlite3.connect('community_nexus.db')
    cursor = db.cursor()
    
    # Today's date
    today = datetime.now().strftime('%Y-%m-%d')
    
    print(f"\n📊 DAILY SALES REPORT - {today}")
    print("=" * 50)
    
    # Total transactions today
    cursor.execute('''
    SELECT COUNT(*), SUM(amount) 
    FROM transactions 
    WHERE date(timestamp) = date('now')
    ''')
    count, total = cursor.fetchone()
    
    if total is None:
        total = 0
    
    print(f"💰 Total Sales Today: R{total:.2f}")
    print(f"📦 Total Transactions: {count or 0}")
    print()
    
    # Transactions by type
    print("📋 Transactions by Type:")
    cursor.execute('''
    SELECT type, COUNT(*), SUM(amount) 
    FROM transactions 
    WHERE date(timestamp) = date('now')
    GROUP BY type
    ''')
    
    for ttype, tcount, tamount in cursor.fetchall():
        if tamount is None:
            tamount = 0
        print(f"   {ttype}: {tcount} transactions, R{tamount:.2f}")
    
    print()
    
    # Marketplace inventory status
    print("🏪 Marketplace Status:")
    cursor.execute('SELECT COUNT(*) FROM marketplace')
    total_items = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(DISTINCT village) FROM marketplace')
    villages_covered = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(DISTINCT category) FROM marketplace')
    categories = cursor.fetchone()[0]
    
    print(f"   Total Items: {total_items}")
    print(f"   Villages Covered: {villages_covered}")
    print(f"   Categories: {categories}")
    print()
    
    # Top villages by inventory
    print("🏆 Top Villages by Inventory:")
    cursor.execute('''
    SELECT village, COUNT(*) as items 
    FROM marketplace 
    GROUP BY village 
    ORDER BY items DESC 
    LIMIT 5
    ''')
    
    for village, items in cursor.fetchall():
        print(f"   {village}: {items} items")
    
    print("\n" + "=" * 50)
    print("✅ Report generated successfully!")
    
    # Save to file
    with open(f'daily_report_{today}.txt', 'w') as f:
        f.write(f"Daily Sales Report - {today}\n")
        f.write(f"Total Sales: R{total:.2f}\n")
        f.write(f"Transactions: {count or 0}\n")
        f.write(f"Marketplace Items: {total_items}\n")
    
    db.close()

if __name__ == "__main__":
    generate_daily_report()
