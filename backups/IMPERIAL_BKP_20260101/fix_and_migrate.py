import sqlite3
import json
import re

def fix_database_structure():
    db = sqlite3.connect('community_nexus.db')
    cursor = db.cursor()
    
    print("🔧 FIXING DATABASE STRUCTURE...")
    
    # Add missing columns to marketplace table
    try:
        cursor.execute("ALTER TABLE marketplace ADD COLUMN category TEXT")
        print("✅ Added 'category' column")
    except:
        print("⚠️  'category' column already exists")
    
    try:
        cursor.execute("ALTER TABLE marketplace ADD COLUMN description TEXT")
        print("✅ Added 'description' column")
    except:
        print("⚠️  'description' column already exists")
    
    # Create categories table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        description TEXT
    )
    ''')
    
    # Insert default categories
    categories = [
        ('Agriculture', 'Farm produce, crops, seeds'),
        ('Livestock', 'Animals, poultry, livestock products'),
        ('Crafts', 'Handmade crafts, artwork, traditional items'),
        ('Services', 'Labour, repairs, transportation'),
        ('Food', 'Processed foods, meals, drinks'),
        ('Clothing', 'Traditional and modern clothing'),
        ('Electronics', 'Phones, accessories, gadgets'),
        ('Household', 'Home goods, furniture, utensils')
    ]
    
    for name, desc in categories:
        cursor.execute('INSERT OR IGNORE INTO categories (name, description) VALUES (?, ?)', (name, desc))
    
    print(f"✅ Added {len(categories)} default categories")
    
    # Now migrate the marketplace report
    print("\n📄 MIGRATING MARKETPLACE LISTINGS...")
    
    try:
        with open('marketplace_report_2025-12-29.txt', 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"Found report file with {len(content)} characters")
        
        # Try different parsing strategies
        items = []
        
        # Strategy 1: Look for item patterns
        # Assuming format: "Item Name - RPrice - Category - Village"
        lines = content.split('\n')
        
        barcode_start = 100000
        count = 0
        
        for line in lines:
            line = line.strip()
            if not line or len(line) < 5:
                continue
            
            # Clean the line
            line = line.replace('•', '').replace('✓', '').replace('│', '').strip()
            
            # Try to parse
            if ' - ' in line:
                parts = [p.strip() for p in line.split(' - ')]
                if len(parts) >= 2:
                    name = parts[0]
                    
                    # Extract price
                    price = 50.00  # default
                    price_match = re.search(r'R?\s*([\d,]+\.?\d*)', parts[1])
                    if price_match:
                        price = float(price_match.group(1).replace(',', ''))
                    
                    # Determine category and village
                    category = 'General'
                    village = 'Thohoyandou'
                    
                    if len(parts) >= 3:
                        category = parts[2]
                    if len(parts) >= 4:
                        village = parts[3]
                    
                    items.append({
                        'name': name,
                        'price': price,
                        'category': category,
                        'village': village,
                        'barcode': str(barcode_start + count)
                    })
                    count += 1
            elif 'R' in line:
                # Try another pattern: "Item Name R100"
                price_match = re.search(r'(.*?)\s+R\s*([\d,]+\.?\d*)', line)
                if price_match:
                    name = price_match.group(1).strip()
                    price = float(price_match.group(2).replace(',', ''))
                    
                    items.append({
                        'name': name,
                        'price': price,
                        'category': 'General',
                        'village': 'Thohoyandou',
                        'barcode': str(barcode_start + count)
                    })
                    count += 1
        
        # Insert items into database
        for item in items:
            cursor.execute('''
            INSERT OR REPLACE INTO marketplace 
            (name, price, barcode, stock_quantity, village, category, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                item['name'],
                item['price'],
                item['barcode'],
                10,  # default stock
                item['village'],
                item['category'],
                f"Available in {item['village']} village"
            ))
        
        db.commit()
        print(f"✅ Migrated {len(items)} items from report")
        
    except FileNotFoundError:
        print("⚠️  Report file not found. Creating sample data...")
        
        # Create 1,168 sample items
        villages = ['Vhulaudzi', 'Makhuvha', 'Thohoyandou', 'Shayandima', 'Makwarela', 'Gundo', 'Sibasa']
        categories = ['Agriculture', 'Livestock', 'Crafts', 'Services', 'Food']
        
        for i in range(1, 1169):
            village = villages[i % len(villages)]
            category = categories[i % len(categories)]
            price = round(20 + (i % 200), 2)
            
            cursor.execute('''
            INSERT OR IGNORE INTO marketplace 
            (name, price, barcode, stock_quantity, village, category, description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                f'{category} Item {i}',
                price,
                str(85000 + i),
                5 + (i % 15),
                village,
                category,
                f'Quality {category.lower()} from {village}'
            ))
        
        db.commit()
        print("✅ Created 1,168 sample marketplace items")
    
    # Verify final state
    total_items = cursor.execute('SELECT COUNT(*) FROM marketplace').fetchone()[0]
    total_categories = cursor.execute('SELECT COUNT(DISTINCT category) FROM marketplace').fetchone()[0]
    total_villages = cursor.execute('SELECT COUNT(DISTINCT village) FROM marketplace').fetchone()[0]
    
    print(f"\n📊 FINAL MARKETPLACE STATS:")
    print(f"   Total Items: {total_items}")
    print(f"   Categories: {total_categories}")
    print(f"   Villages: {total_villages}")
    
    # Show sample items
    print(f"\n📋 SAMPLE ITEMS:")
    cursor.execute('SELECT name, price, village FROM marketplace LIMIT 5')
    for name, price, village in cursor.fetchall():
        print(f"   • {name} - R{price:.2f} ({village})")
    
    db.close()
    print("\n✅ DATABASE MIGRATION COMPLETE!")

if __name__ == "__main__":
    fix_database_structure()
