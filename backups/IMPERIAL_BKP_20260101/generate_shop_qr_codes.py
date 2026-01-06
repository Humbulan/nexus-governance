import sqlite3
import qrcode
import os
from datetime import datetime

def generate_qr_codes():
    print("🖨️  GENERATING QR CODES FOR SHOP WINDOWS")
    print("=" * 50)
    
    # Create output directory
    if not os.path.exists('shop_qr_codes'):
        os.makedirs('shop_qr_codes')
    
    # Connect to database
    db = sqlite3.connect('community_nexus.db')
    cursor = db.cursor()
    
    # Get popular items from each village
    cursor.execute('''
    SELECT m.name, m.price, m.barcode, m.village, m.category,
           (SELECT COUNT(*) FROM marketplace m2 
            WHERE m2.village = m.village) as village_items
    FROM marketplace m
    WHERE m.barcode IN (
        SELECT barcode FROM marketplace 
        GROUP BY village 
        HAVING COUNT(*) = 1  # Get one unique item per village
        LIMIT 20
    )
    ORDER BY m.village
    ''')
    
    items = cursor.fetchall()
    
    print(f"📊 Generating QR codes for {len(items)} popular items")
    print(f"📁 Output folder: shop_qr_codes/")
    print()
    
    generated_codes = []
    
    for name, price, barcode, village, category, village_items in items:
        # Create USSD command for this item
        ussd_command = f"*134*600#*{barcode}*"
        
        # Create display text
        display_text = f"""
        🏪 HUMBU COMMUNITY NEXUS
        📍 {village.upper()}
        📦 {name}
        💰 R{price:.2f}
        🏷️  Barcode: {barcode}
        📱 Dial: {ussd_command}
        🌍 {village_items} items available
        """
        
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(ussd_command)
        qr.make(fit=True)
        
        # Create image
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save QR code
        filename = f"shop_qr_codes/{village}_{barcode}.png"
        img.save(filename)
        
        # Save display card
        card_filename = f"shop_qr_codes/{village}_{barcode}_card.txt"
        with open(card_filename, 'w') as f:
            f.write(display_text)
        
        generated_codes.append({
            'village': village,
            'item': name,
            'price': price,
            'barcode': barcode,
            'qr_file': filename,
            'card_file': card_filename
        })
        
        print(f"✅ Generated: {village} - {name} (R{price:.2f})")
    
    db.close()
    
    # Create a master index
    with open('shop_qr_codes/INDEX.md', 'w') as f:
        f.write("# HUMBU COMMUNITY NEXUS - SHOP QR CODES\n")
        f.write(f"## Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## How to Use:\n")
        f.write("1. Print the PNG files and display in shop windows\n")
        f.write("2. Customers scan QR code with phone camera\n")
        f.write("3. Phone automatically dials the USSD command\n")
        f.write("4. Complete purchase via MTN MoMo\n\n")
        
        f.write("## Village QR Codes:\n")
        for item in generated_codes:
            f.write(f"### {item['village']}\n")
            f.write(f"- **Item**: {item['item']}\n")
            f.write(f"- **Price**: R{item['price']:.2f}\n")
            f.write(f"- **Barcode**: {item['barcode']}\n")
            f.write(f"- **QR Code**: [{item['village']}_{item['barcode']}.png]({item['village']}_{item['barcode']}.png)\n")
            f.write(f"- **Display Card**: [{item['village']}_{item['barcode']}_card.txt]({item['village']}_{item['barcode']}_card.txt)\n")
            f.write(f"- **USSD Command**: `{f'*134*600#*{item['barcode']}*'}`\n\n")
    
    print(f"\n📝 Master index created: shop_qr_codes/INDEX.md")
    
    # Generate a sample for Thohoyandou (the hub)
    print(f"\n🎯 SAMPLE FOR THOHOYANDOU HUB:")
    cursor = db.cursor()
    cursor.execute('''
    SELECT name, price, barcode, category 
    FROM marketplace 
    WHERE village = 'THOHOYANDOU' 
    LIMIT 3
    ''')
    
    thohoyandou_items = cursor.fetchall()
    
    for name, price, barcode, category in thohoyandou_items:
        print(f"   • {name} - R{price:.2f} (Barcode: {barcode})")
        print(f"     USSD: *134*600#*{barcode}*")
    
    db.close()
    
    print(f"\n" + "=" * 50)
    print("✅ QR CODE GENERATION COMPLETE!")
    print("=" * 50)
    print("🏪 Print and display in shop windows")
    print("📱 Customers scan with phone camera")
    print("💰 Automatic USSD dialing")
    print("🌍 Professional presence in all 40 villages")
    print(f"\n📁 Files generated in: shop_qr_codes/")

if __name__ == "__main__":
    generate_qr_codes()
