#! /usr/bin/env python3
#!/data/data/com.termux/files/usr/bin/python3
"""
HUMBU COMMUNITY NEXUS - PEOPLE'S PLATFORM
Transforms $148K success into community economic engine
"""

import json
import os
import sys
import random
import time
import threading
import socket
import sqlite3
from datetime import datetime
from pathlib import Path

class CommunityNexus:
    def __init__(self):
        # Core directories
        self.base_dir = Path.home() / "humbu_community_nexus"
        self.data_dir = self.base_dir / "data"
        self.marketplace_dir = self.base_dir / "marketplace"
        self.tasks_dir = self.base_dir / "tasks"
        self.wallets_dir = self.base_dir / "wallets"
        
        # Ensure directories exist
        for dir_path in [self.data_dir, self.marketplace_dir, self.tasks_dir, self.wallets_dir]:
            dir_path.mkdir(exist_ok=True)
        
        # Initialize database
        self.db_path = self.data_dir / "community.db"
        self.init_database()
        
        # Thohoyandou base coordinates
        self.thohoyandou_coords = {
            "lat": -22.9756,
            "lon": 30.4591,
            "radius_km": 50  # Cover surrounding villages
        }
        
        # Village coordinates around Thohoyandou
        self.villages = {
            "thohoyandou": {"lat": -22.9756, "lon": 30.4591},
            "manini": {"lat": -22.9208, "lon": 30.4325},
            "sibasa": {"lat": -22.9439, "lon": 30.4681},
            "mukhomi": {"lat": -22.8767, "lon": 30.4186},
            "malamulele": {"lat": -22.9847, "lon": 30.6844},
            "gundo": {"lat": -22.8125, "lon": 30.5083},
            "makhuvha": {"lat": -23.0389, "lon": 30.2931},
            "folovhodwe": {"lat": -23.0319, "lon": 30.4103},
            "vhulaudzi": {"lat": -23.0917, "lon": 30.3250},
            "shitale": {"lat": -22.8100, "lon": 30.3500}
        }
        
        # Marketplace categories (aligned with local economy)
        self.categories = {
            "agriculture": ["maize", "tomatoes", "spinach", "cabbage", "pumpkin", "beans"],
            "livestock": ["chickens", "goats", "pigs", "rabbits", "eggs"],
            "handicrafts": ["baskets", "mats", "pottery", "wood_carvings"],
            "services": ["plumbing", "electrical", "transport", "repairs"],
            "food": ["pap", "bread", "snacks", "traditional_meals"]
        }
        
        print("🏗️ HUMBU COMMUNITY NEXUS INITIALIZED")
        print("🌍 Connecting villages around Thohoyandou")
        print(f"📍 Villages: {len(self.villages)}")
        print(f"📦 Categories: {len(self.categories)}")
    
    def init_database(self):
        """Initialize SQLite database for community data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT UNIQUE,
            village TEXT,
            role TEXT,
            wallet_balance REAL DEFAULT 0.0,
            rating REAL DEFAULT 5.0,
            verified INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Marketplace listings
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS listings (
            id TEXT PRIMARY KEY,
            user_id TEXT,
            category TEXT,
            item TEXT,
            description TEXT,
            price REAL,
            quantity INTEGER,
            unit TEXT,
            location_lat REAL,
            location_lon REAL,
            status TEXT DEFAULT 'available',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        ''')
        
        # Tasks/micro-gigs
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            title TEXT,
            description TEXT,
            category TEXT,
            reward REAL,
            duration_hours INTEGER,
            location_lat REAL,
            location_lon REAL,
            posted_by TEXT,
            assigned_to TEXT,
            status TEXT DEFAULT 'open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        # Transactions
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id TEXT PRIMARY KEY,
            from_user TEXT,
            to_user TEXT,
            amount REAL,
            type TEXT,
            reference TEXT,
            status TEXT DEFAULT 'completed',
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def register_user(self, phone, name, village="thohoyandou", role="trader"):
        """Register a new community user"""
        user_id = f"USER_{phone[-8:]}"
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute("SELECT id FROM users WHERE phone = ?", (phone,))
        existing = cursor.fetchone()
        
        if existing:
            print(f"⚠️ User {phone} already registered")
            return existing[0]
        
        # Get village coordinates
        village_coords = self.villages.get(village, self.villages["thohoyandou"])
        
        # Insert new user with initial wallet balance
        cursor.execute('''
        INSERT INTO users (id, name, phone, village, role, wallet_balance, verified)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, name, phone, village, role, 50.0, 1))
        
        conn.commit()
        conn.close()
        
        print(f"✅ User registered: {name} ({phone}) from {village}")
        print(f"   ID: {user_id}, Initial wallet: R50.00")
        
        return user_id
    
    def create_marketplace_listing(self, user_id, category, item, price, quantity, unit="kg"):
        """Create a marketplace listing"""
        listing_id = f"LIST_{int(time.time())}_{random.randint(1000, 9999)}"
        
        # Get user info
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT village FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        
        if not user:
            print(f"❌ User {user_id} not found")
            return None
        
        village = user[0]
        village_coords = self.villages.get(village, self.villages["thohoyandou"])
        
        # Add some randomness to location within village
        lat = village_coords["lat"] + random.uniform(-0.02, 0.02)
        lon = village_coords["lon"] + random.uniform(-0.02, 0.02)
        
        # Insert listing
        cursor.execute('''
        INSERT INTO listings (id, user_id, category, item, price, quantity, unit, location_lat, location_lon)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (listing_id, user_id, category, item, price, quantity, unit, lat, lon))
        
        conn.commit()
        conn.close()
        
        print(f"📦 Listing created: {item} for R{price}/{unit}")
        print(f"   Location: {village} ({lat:.4f}, {lon:.4f})")
        
        return listing_id
    
    def create_micro_task(self, title, description, category, reward, duration_hours, location_village):
        """Create a micro-task/gig for community members"""
        task_id = f"TASK_{int(time.time())}_{random.randint(1000, 9999)}"
        
        village_coords = self.villages.get(location_village, self.villages["thohoyandou"])
        
        # Add randomness
        lat = village_coords["lat"] + random.uniform(-0.01, 0.01)
        lon = village_coords["lon"] + random.uniform(-0.01, 0.01)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO tasks (id, title, description, category, reward, duration_hours, location_lat, location_lon, posted_by)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (task_id, title, description, category, reward, duration_hours, lat, lon, "SYSTEM"))
        
        conn.commit()
        conn.close()
        
        print(f"🎯 Task created: {title}")
        print(f"   Reward: R{reward}, Location: {location_village}")
        
        return task_id
    
    def generate_sample_community(self, num_users=20, num_listings=30, num_tasks=15):
        """Generate sample community data for demonstration"""
        print("👥 GENERATING SAMPLE COMMUNITY DATA...")
        
        # Sample users from different villages
        sample_users = [
            {"phone": "0721234567", "name": "James Mudau", "village": "thohoyandou", "role": "farmer"},
            {"phone": "0822345678", "name": "Sarah Mulaudzi", "village": "sibasa", "role": "artisan"},
            {"phone": "0713456789", "name": "Thomas Nemadodzi", "village": "manini", "role": "trader"},
            {"phone": "0834567890", "name": "Maria Tshikovhi", "village": "malamulele", "role": "farmer"},
            {"phone": "0725678901", "name": "David Phaswana", "village": "mukhomi", "role": "service"},
            {"phone": "0816789012", "name": "Grace Mabunda", "village": "gundo", "role": "food_vendor"},
            {"phone": "0737890123", "name": "Peter Netshisaulu", "village": "makhuvha", "role": "handyman"},
            {"phone": "0828901234", "name": "Lerato Baloyi", "village": "folovhodwe", "role": "seamstress"}
        ]
        
        # Register users
        user_ids = []
        for user in sample_users[:num_users]:
            uid = self.register_user(**user)
            user_ids.append(uid)
        
        # Create marketplace listings
        print("\n📦 CREATING MARKETPLACE LISTINGS...")
        for _ in range(num_listings):
            user_id = random.choice(user_ids)
            category = random.choice(list(self.categories.keys()))
            item = random.choice(self.categories[category])
            price = round(random.uniform(10, 500), 2)
            quantity = random.randint(1, 20)
            
            self.create_marketplace_listing(
                user_id=user_id,
                category=category,
                item=item,
                price=price,
                quantity=quantity,
                unit="kg" if category == "agriculture" else "each"
            )
        
        # Create micro-tasks
        print("\n🎯 CREATING MICRO-TASKS...")
        task_templates = [
            {"title": "Water leak reporting", "desc": "Report water leak in your area with photos", "cat": "services", "reward": 50, "hours": 2},
            {"title": "Street cleaning", "desc": "Clean 100m of street in your neighborhood", "cat": "services", "reward": 150, "hours": 4},
            {"title": "Delivery assistance", "desc": "Help deliver packages within village", "cat": "services", "reward": 100, "hours": 3},
            {"title": "Crop monitoring", "desc": "Monitor and report on community garden", "cat": "agriculture", "reward": 80, "hours": 2},
            {"title": "Local survey", "desc": "Survey 10 households about community needs", "cat": "services", "reward": 200, "hours": 5}
        ]
        
        for _ in range(num_tasks):
            task = random.choice(task_templates)
            village = random.choice(list(self.villages.keys()))
            
            self.create_micro_task(
                title=task["title"],
                description=task["desc"],
                category=task["cat"],
                reward=task["reward"],
                duration_hours=task["hours"],
                location_village=village
            )
        
        print(f"\n✅ SAMPLE COMMUNITY CREATED:")
        print(f"   👥 Users: {len(user_ids)}")
        print(f"   📦 Listings: {num_listings}")
        print(f"   🎯 Tasks: {num_tasks}")
        print(f"   🌍 Villages: {len(self.villages)}")
    
    def get_community_stats(self):
        """Get community platform statistics"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        stats = {}
        
        # Count users
        cursor.execute("SELECT COUNT(*) FROM users")
        stats["total_users"] = cursor.fetchone()[0]
        
        # Count listings
        cursor.execute("SELECT COUNT(*) FROM listings WHERE status = 'available'")
        stats["active_listings"] = cursor.fetchone()[0]
        
        # Count tasks
        cursor.execute("SELECT COUNT(*) FROM tasks WHERE status = 'open'")
        stats["open_tasks"] = cursor.fetchone()[0]
        
        # Total wallet value
        cursor.execute("SELECT SUM(wallet_balance) FROM users")
        total_wallet = cursor.fetchone()[0] or 0
        stats["total_wallet_value"] = total_wallet
        
        # Recent transactions
        cursor.execute("SELECT COUNT(*) FROM transactions WHERE timestamp > datetime('now', '-7 days')")
        stats["weekly_transactions"] = cursor.fetchone()[0]
        
        conn.close()
        
        return stats
    
    def generate_opportunity_map(self):
        """Generate interactive map data for community opportunities"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        map_data = {
            "type": "FeatureCollection",
            "features": []
        }
        
        # Add village markers
        for village_name, coords in self.villages.items():
            feature = {
                "type": "Feature",
                "properties": {
                    "name": village_name.upper(),
                    "type": "village",
                    "population": random.randint(500, 5000),
                    "description": f"Community hub in {village_name}"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [coords["lon"], coords["lat"]]
                }
            }
            map_data["features"].append(feature)
        
        # Add marketplace listings
        cursor.execute("""
        SELECT l.item, l.price, l.quantity, l.unit, l.location_lon, l.location_lat, u.name, u.village
        FROM listings l
        JOIN users u ON l.user_id = u.id
        WHERE l.status = 'available'
        LIMIT 50
        """)
        
        for row in cursor.fetchall():
            feature = {
                "type": "Feature",
                "properties": {
                    "name": row[0],
                    "type": "marketplace",
                    "price": f"R{row[1]}",
                    "quantity": f"{row[2]} {row[3]}",
                    "seller": row[6],
                    "village": row[7],
                    "icon": "market"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [row[4], row[5]]
                }
            }
            map_data["features"].append(feature)
        
        # Add tasks
        cursor.execute("""
        SELECT title, reward, location_lon, location_lat, category
        FROM tasks
        WHERE status = 'open'
        LIMIT 30
        """)
        
        for row in cursor.fetchall():
            feature = {
                "type": "Feature",
                "properties": {
                    "name": row[0],
                    "type": "task",
                    "reward": f"R{row[1]}",
                    "category": row[4],
                    "icon": "task"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [row[2], row[3]]
                }
            }
            map_data["features"].append(feature)
        
        conn.close()
        
        # Save to file
        map_file = self.base_dir / "community_map.json"
        with open(map_file, 'w') as f:
            json.dump(map_data, f, indent=2)
        
        print(f"🗺️ Opportunity map generated: {len(map_data['features'])} features")
        
        return map_data

def main():
    """Main execution"""
    print("=" * 60)
    print("🏗️ HUMBU COMMUNITY NEXUS - PEOPLE'S PLATFORM")
    print("🌍 Economic Engine for Limpopo Villages")
    print("=" * 60)
    
    nexus = CommunityNexus()
    
    # Generate sample data for demonstration
    nexus.generate_sample_community(num_users=8, num_listings=15, num_tasks=8)
    
    # Generate opportunity map
    map_data = nexus.generate_opportunity_map()
    
    # Show community statistics
    stats = nexus.get_community_stats()
    
    print("\n📊 COMMUNITY PLATFORM STATISTICS:")
    print("=" * 40)
    for key, value in stats.items():
        key_display = key.replace('_', ' ').title()
        if "wallet" in key:
            print(f"{key_display}: R{value:,.2f}")
        else:
            print(f"{key_display}: {value}")
    
    print("\n🎯 PLATFORM READY FOR:")
    print("   1. 📱 USSD Interface: *134*600# (Coming soon)")
    print("   2. 🌐 Web Portal: http://localhost:8086")
    print("   3. 📍 Opportunity Map: ~/humbu_community_nexus/community_map.json")
    print("   4. 💰 Community Wallets: R{stats['total_wallet_value']:,.2f} in circulation")
    
    print("\n🚀 NEXT STEPS:")
    print("   - Launch web portal with 'python3 community_web.py'")
    print("   - Register first 100 community members")
    print("   - Connect to mobile money APIs")
    print("   - Deploy to Thohoyandou villages")

if __name__ == "__main__":
    main()
