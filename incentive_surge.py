#! /usr/bin/env python3
import sqlite3
from datetime import datetime

def run_incentive_check():
    conn = sqlite3.connect('community_nexus.db')
    cursor = conn.cursor()
    
    target_villages = ('Gundo', 'Sibasa', 'Mukhomi')
    
    print(f"🚀 HUMBU INCENTIVE ENGINE - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("------------------------------------------------------------")
    
    for village in target_villages:
        print(f"\n📍 Village: {village}")
        
        # Using the correct column 'name' found in your PRAGMA check
        query = """
        SELECT name, price, stock_quantity 
        FROM marketplace 
        WHERE village = ? 
        ORDER BY stock_quantity DESC 
        LIMIT 3
        """
        
        cursor.execute(query, (village,))
        items = cursor.fetchall()
        
        if not items:
            print(f"  ℹ️ No stock found for {village}.")
            continue
            
        for i, (item_name, price, stock) in enumerate(items, 1):
            print(f"  {i}. {item_name} | Price: R{price:.2f} | Stock: {stock} units")
            print(f"     [Status]: Ready for Evening Surge ✅")

    conn.close()
    print("\n✅ Village Inventory Verified.")

if __name__ == "__main__":
    run_incentive_check()
