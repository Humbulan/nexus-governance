#!/data/data/com.termux/files/usr/bin/python3
"""
MASS USER REGISTRATION SYSTEM
Add 100 community members with realistic profiles
"""

import sqlite3
import random
import time
from datetime import datetime
from pathlib import Path

def generate_100_users():
    """Generate 100 realistic community user profiles"""
    
    db_path = Path.home() / "humbu_community_nexus" / "data" / "community.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("👥 GENERATING 100 COMMUNITY MEMBERS...")
    print("🌍 Villages around Thohoyandou")
    print("=" * 50)
    
    # Extended village list
    villages = {
        "thohoyandou": {"population": 25000, "center_lat": -22.9756, "center_lon": 30.4591},
        "sibasa": {"population": 8000, "center_lat": -22.9439, "center_lon": 30.4681},
        "manini": {"population": 5000, "center_lat": -22.9208, "center_lon": 30.4325},
        "mukhomi": {"population": 3000, "center_lat": -22.8767, "center_lon": 30.4186},
        "malamulele": {"population": 12000, "center_lat": -22.9847, "center_lon": 30.6844},
        "gundo": {"population": 2000, "center_lat": -22.8125, "center_lon": 30.5083},
        "makhuvha": {"population": 1500, "center_lat": -23.0389, "center_lon": 30.2931},
        "folovhodwe": {"population": 1800, "center_lat": -23.0319, "center_lon": 30.4103},
        "vhulaudzi": {"population": 1200, "center_lat": -23.0917, "center_lon": 30.3250},
        "shitale": {"population": 2500, "center_lat": -22.8100, "center_lon": 30.3500},
        "tshitavha": {"population": 1800, "center_lat": -22.8500, "center_lon": 30.4800},
        "mbilwi": {"population": 2200, "center_lat": -22.8900, "center_lon": 30.5200},
        "lwamondo": {"population": 3500, "center_lat": -22.9300, "center_lon": 30.5500},
        "mukula": {"population": 2800, "center_lat": -22.9600, "center_lon": 30.5800},
        "tshilapfa": {"population": 1500, "center_lat": -23.0500, "center_lon": 30.3500}
    }
    
    # Common Venda names
    first_names = [
        "James", "Sarah", "Thomas", "Maria", "David", "Grace", "Peter", "Lerato",
        "John", "Anna", "Michael", "Susan", "Robert", "Mary", "William", "Patricia",
        "Richard", "Jennifer", "Joseph", "Linda", "Charles", "Elizabeth", "Daniel", "Barbara",
        "Paul", "Nancy", "Mark", "Lisa", "Donald", "Margaret", "George", "Sandra"
    ]
    
    surnames = [
        "Mudau", "Mulaudzi", "Nemadodzi", "Tshikovhi", "Phaswana", "Mabunda", "Netshisaulu", "Baloyi",
        "Makhado", "Ralushai", "Mutele", "Tshivhase", "Mphaphuli", "Makuya", "Nethengwe", "Tshikororo",
        "Magidi", "Mathidi", "Tshililo", "Muthelo", "Tshamano", "Mavhungu", "Mutele", "Tshikalange"
    ]
    
    roles = [
        ("farmer", 0.35),        # 35% farmers
        ("trader", 0.20),        # 20% traders
        ("artisan", 0.15),       # 15% artisans
        ("service", 0.10),       # 10% service providers
        ("food_vendor", 0.08),   # 8% food vendors
        ("student", 0.07),       # 7% students
        ("elder", 0.05)         # 5% elders
    ]
    
    # Generate 100 users
    users_added = 0
    for i in range(1, 101):
        # Generate user data
        first_name = random.choice(first_names)
        surname = random.choice(surnames)
        full_name = f"{first_name} {surname}"
        
        # Generate phone number (South African format)
        prefix = random.choice(["072", "073", "074", "076", "079", "082", "083", "084"])
        number = f"{prefix}{random.randint(1000000, 9999999)}"
        
        # Select village based on population distribution
        village = random.choices(
            list(villages.keys()),
            weights=[v["population"] for v in villages.values()]
        )[0]
        
        # Select role based on distribution
        role = random.choices(
            [r[0] for r in roles],
            weights=[r[1] for r in roles]
        )[0]
        
        # Initial wallet balance (farmers and traders get more)
        if role in ["farmer", "trader"]:
            wallet_balance = round(random.uniform(50, 200), 2)
        elif role == "elder":
            wallet_balance = round(random.uniform(100, 300), 2)
        else:
            wallet_balance = round(random.uniform(20, 100), 2)
        
        # User ID
        user_id = f"USER_{number[-8:]}"
        
        try:
            # Insert user
            cursor.execute('''
            INSERT INTO users (id, name, phone, village, role, wallet_balance, verified, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_id,
                full_name,
                number,
                village,
                role,
                wallet_balance,
                1,
                datetime.now().isoformat()
            ))
            
            users_added += 1
            
            # Show progress
            if i % 10 == 0:
                print(f"✅ Registered {i}/100 users...")
                
        except sqlite3.IntegrityError:
            # Skip if phone number already exists
            continue
    
    conn.commit()
    
    # Generate listings for new users
    print("\n📦 GENERATING LISTINGS FOR NEW USERS...")
    generate_listings_for_users(cursor, users_added)
    
    conn.commit()
    conn.close()
    
    # Update stats
    print("\n📊 UPDATING PLATFORM STATISTICS...")
    update_platform_stats()
    
    print(f"\n🎉 MASS REGISTRATION COMPLETE!")
    print(f"   👥 {users_added} new users registered")
    print(f"   📦 Additional listings created")
    print(f"   💰 Total wallet value increased")
    print(f"   🌍 Platform now serves 15 villages")

def generate_listings_for_users(cursor, user_count):
    """Generate marketplace listings for new users"""
    
    categories = {
        "agriculture": ["maize", "tomatoes", "spinach", "cabbage", "pumpkin", "beans", "potatoes", "onions", "carrots", "lettuce"],
        "livestock": ["chickens", "goats", "pigs", "rabbits", "eggs", "milk", "wool", "honey"],
        "handicrafts": ["baskets", "mats", "pottery", "wood_carvings", "beadwork", "clothing", "jewelry"],
        "services": ["plumbing", "electrical", "transport", "repairs", "construction", "tutoring", "translation"],
        "food": ["pap", "bread", "snacks", "traditional_meals", "catering", "preserves"]
    }
    
    # Generate 2-3 listings per user
    total_listings = 0
    cursor.execute("SELECT id, village, role FROM users ORDER BY RANDOM() LIMIT ?", (user_count * 2,))
    users = cursor.fetchall()
    
    for user_id, village, role in users:
        # Select appropriate category based on role
        if role == "farmer":
            category = random.choice(["agriculture", "livestock"])
        elif role == "artisan":
            category = "handicrafts"
        elif role == "food_vendor":
            category = "food"
        else:
            category = random.choice(list(categories.keys()))
        
        item = random.choice(categories[category])
        
        # Generate realistic price
        if category == "agriculture":
            price = round(random.uniform(20, 500), 2)
            quantity = random.randint(1, 50)
            unit = "kg"
        elif category == "livestock":
            price = round(random.uniform(100, 2000), 2)
            quantity = random.randint(1, 10)
            unit = "each"
        elif category == "handicrafts":
            price = round(random.uniform(50, 1000), 2)
            quantity = random.randint(1, 5)
            unit = "each"
        else:
            price = round(random.uniform(50, 500), 2)
            quantity = 1
            unit = "service"
        
        # Generate listing ID
        listing_id = f"LIST_{int(time.time())}_{random.randint(10000, 99999)}"
        
        # Insert listing
        cursor.execute('''
        INSERT INTO listings (id, user_id, category, item, price, quantity, unit, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            listing_id,
            user_id,
            category,
            item,
            price,
            quantity,
            unit,
            "available",
            datetime.now().isoformat()
        ))
        
        total_listings += 1
    
    print(f"   Created {total_listings} new marketplace listings")

def update_platform_stats():
    """Update platform statistics after mass registration"""
    
    db_path = Path.home() / "humbu_community_nexus" / "data" / "community.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get new totals
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM listings WHERE status = 'available'")
    total_listings = cursor.fetchone()[0]
    
    cursor.execute("SELECT SUM(wallet_balance) FROM users")
    total_wallet = cursor.fetchone()[0] or 0
    
    cursor.execute("SELECT COUNT(DISTINCT village) FROM users")
    villages_covered = cursor.fetchone()[0]
    
    conn.close()
    
    print(f"\n📊 UPDATED PLATFORM STATISTICS:")
    print(f"   👥 Total Users: {total_users}")
    print(f"   📦 Total Listings: {total_listings}")
    print(f"   💰 Total Wallet Value: R{total_wallet:.2f}")
    print(f"   🌍 Villages Covered: {villages_covered}")

if __name__ == "__main__":
    generate_100_users()
    
    # Create welcome message file
    welcome_file = Path.home() / "humbu_community_nexus" / "welcome_100_users.md"
    with open(welcome_file, 'w') as f:
        f.write(f"""# 🎉 WELCOME TO 100 COMMUNITY MEMBERS!

## 📊 Platform Statistics (After Mass Registration)
- **Total Users:** {total_users if 'total_users' in locals() else 'N/A'}
- **Marketplace Listings:** {total_listings if 'total_listings' in locals() else 'N/A'}
- **Total Wallet Value:** R{total_wallet if 'total_wallet' in locals() else 'N/A'}
- **Villages Covered:** {villages_covered if 'villages_covered' in locals() else 'N/A'}

## 🚀 Next Steps
1. Mobile Money Integration (Next Phase)
2. USSD Interface Launch
3. Physical Deployment Planning
4. Community Training Sessions

*Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
""")
    
    print(f"\n📝 Welcome document saved: {welcome_file}")
