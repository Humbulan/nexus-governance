#! /usr/bin/env python3
import qrcode
import sqlite3
import os

# 1. Setup folders
if not os.path.exists('nexus_print_shop'):
    os.makedirs('nexus_print_shop')

# 2. Connect to your database
db = sqlite3.connect('community_nexus.db')
cursor = db.cursor()

# 3. Fetch top items (Using a clean query to avoid 'unrecognized token' errors)
query = "SELECT barcode, name, village, price FROM marketplace WHERE price > 0 LIMIT 15"
cursor.execute(query)
items = cursor.fetchall()

print("🚀 STARTING QR PRODUCTION FOR VHEMBE DISTRICT...")
print("=" * 50)

for barcode, name, village, price in items:
    # Create the QR content
    # Format: USSD Code + Barcode + Brand
    content = f"DIAL:*134*600#\nBARCODE:{barcode}\nITEM:{name}\nPRICE:R{price}"
    
    # Generate QR
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(content)
    qr.make(fit=True)
    
    # Save Image
    img = qr.make_image(fill_color="black", back_color="white")
    clean_name = name.split('(')[0].strip().replace(' ', '_')
    filename = f"nexus_print_shop/{village}_{clean_name}.png"
    img.save(filename)
    
    print(f"✅ Created: {village} - {name} (R{price})")

db.close()
print("\n📦 SUCCESS! Check the 'nexus_print_shop' folder for your printable assets.")
print("🖨️  Files available in: nexus_print_shop/")
