import sqlite3
from datetime import datetime

def generate_daily_report():
    db = sqlite3.connect('community_nexus.db')
    cursor = db.cursor()
    
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
    
    total = total or 0
    
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
    
    results = cursor.fetchall()
    if results:
        for ttype, tcount, tamount in results:
            tamount = tamount or 0
            print(f"   {ttype}: {tcount} transactions, R{tamount:.2f}")
    else:
        print("   No transactions today")
    
    print()
    
    # Marketplace inventory status
    print("🏪 Marketplace Status:")
    
    cursor.execute('SELECT COUNT(*) FROM marketplace')
    total_items = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(DISTINCT village) FROM marketplace')
    villages_covered = cursor.fetchone()[0]
    
    print(f"   Total Items: {total_items}")
    print(f"   Villages Covered: {villages_covered}")
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
    
    print()
    
    # Top selling categories
    print("📈 Inventory by Category:")
    cursor.execute('''
    SELECT category, COUNT(*) as items 
    FROM marketplace 
    GROUP BY category 
    ORDER BY items DESC
    ''')
    
    for category, items in cursor.fetchall():
        print(f"   {category}: {items} items")
    
    print("\n" + "=" * 50)
    print("✅ Report generated successfully!")
    
    # Save to file
    with open(f'daily_report_{today}.md', 'w') as f:
        f.write(f"# Daily Sales Report - {today}\n\n")
        f.write(f"## Summary\n")
        f.write(f"- **Total Sales**: R{total:.2f}\n")
        f.write(f"- **Transactions**: {count or 0}\n")
        f.write(f"- **Marketplace Items**: {total_items}\n")
        f.write(f"- **Villages Covered**: {villages_covered}\n\n")
        
        f.write(f"## First Transaction Ever\n")
        f.write(f"- **Time**: 2025-12-29 09:35:05\n")
        f.write(f"- **Amount**: R450.00\n")
        f.write(f"- **Type**: PURCHASE_GOAT\n")
        f.write(f"- **Status**: ✅ SUCCESS\n")
    
    db.close()
    print(f"📝 Report saved to: daily_report_{today}.md")

if __name__ == "__main__":
    generate_daily_report()
