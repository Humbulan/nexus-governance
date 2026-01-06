#! /usr/bin/env python3
#!/usr/bin/env python3
"""
Weekly automated backup script for Humbu Community Nexus
Run this every Sunday at midnight using cron
"""

import sqlite3
import json
import csv
import os
import shutil
from datetime import datetime, timedelta
import sys

def weekly_backup():
    print("🔒 HUMBU COMMUNITY NEXUS - WEEKLY AUTOMATED BACKUP")
    print("=" * 60)
    print(f"Backup started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Create backup directory with week number
    now = datetime.now()
    week_num = now.isocalendar()[1]
    year = now.year
    backup_dir = f"weekly_backups/{year}_week_{week_num}"
    
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    
    try:
        # 1. Full database backup
        print("📦 Creating full database backup...")
        db_backup = f"{backup_dir}/community_nexus_{timestamp}.db"
        shutil.copy2("community_nexus.db", db_backup)
        print(f"   ✅ Database backup: {db_backup}")
        
        # 2. SQL dump
        print("💾 Creating SQL dump...")
        sql_dump = f"{backup_dir}/community_nexus_{timestamp}.sql"
        os.system(f'sqlite3 community_nexus.db .dump > "{sql_dump}"')
        print(f"   ✅ SQL dump: {sql_dump}")
        
        # 3. JSON exports
        print("📊 Exporting data to JSON...")
        
        # Export transactions
        conn = sqlite3.connect('community_nexus.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM transactions")
        transactions = cursor.fetchall()
        cursor.execute("PRAGMA table_info(transactions)")
        tx_columns = [col[1] for col in cursor.fetchall()]
        
        tx_data = []
        for tx in transactions:
            tx_dict = {tx_columns[i]: tx[i] for i in range(len(tx_columns))}
            tx_data.append(tx_dict)
        
        with open(f"{backup_dir}/transactions_{timestamp}.json", 'w') as f:
            json.dump(tx_data, f, indent=2, default=str)
        print(f"   ✅ Transactions: {len(tx_data)} records")
        
        # Export marketplace
        cursor.execute("SELECT * FROM marketplace")
        marketplace = cursor.fetchall()
        cursor.execute("PRAGMA table_info(marketplace)")
        mp_columns = [col[1] for col in cursor.fetchall()]
        
        mp_data = []
        for item in marketplace:
            item_dict = {mp_columns[i]: item[i] for i in range(len(mp_columns))}
            mp_data.append(item_dict)
        
        with open(f"{backup_dir}/marketplace_{timestamp}.json", 'w') as f:
            json.dump(mp_data, f, indent=2, default=str)
        print(f"   ✅ Marketplace: {len(mp_data)} items")
        
        # 4. Weekly statistics report
        print("📈 Generating weekly statistics...")
        
        cursor.execute("SELECT COUNT(*) FROM transactions WHERE date(timestamp) >= date('now', '-7 days')")
        weekly_tx = cursor.fetchone()[0]
        
        cursor.execute("SELECT SUM(amount) FROM transactions WHERE date(timestamp) >= date('now', '-7 days')")
        weekly_value = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(DISTINCT village) FROM marketplace")
        villages = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM marketplace")
        total_items = cursor.fetchone()[0]
        
        conn.close()
        
        # 5. Create weekly report
        report = {
            "backup_date": now.isoformat(),
            "week_number": week_num,
            "year": year,
            "statistics": {
                "weekly_transactions": weekly_tx,
                "weekly_value": float(weekly_value),
                "total_villages": villages,
                "total_marketplace_items": total_items,
                "new_items_this_week": 0,  # Would track in production
                "new_transactions_this_week": weekly_tx
            },
            "backup_files": {
                "database": db_backup,
                "sql_dump": sql_dump,
                "transactions_json": f"{backup_dir}/transactions_{timestamp}.json",
                "marketplace_json": f"{backup_dir}/marketplace_{timestamp}.json"
            }
        }
        
        with open(f"{backup_dir}/weekly_report_{timestamp}.json", 'w') as f:
            json.dump(report, f, indent=2)
        
        # 6. Clean old backups (keep 8 weeks = 2 months)
        print("🧹 Cleaning old backups...")
        backups_dir = "weekly_backups"
        if os.path.exists(backups_dir):
            for item in os.listdir(backups_dir):
                item_path = os.path.join(backups_dir, item)
                if os.path.isdir(item_path):
                    try:
                        # Extract week number from folder name
                        parts = item.split('_')
                        if len(parts) >= 3 and parts[0].isdigit():
                            item_year = int(parts[0])
                            item_week = int(parts[2])
                            item_date = datetime.fromisocalendar(item_year, item_week, 1)
                            
                            # Delete if older than 8 weeks
                            if now - item_date > timedelta(weeks=8):
                                shutil.rmtree(item_path)
                                print(f"   🗑️  Deleted old backup: {item}")
                    except:
                        continue
        
        print("\n" + "=" * 60)
        print("✅ WEEKLY BACKUP COMPLETE!")
        print("=" * 60)
        print(f"📁 Backup location: {backup_dir}/")
        print(f"📊 Weekly Statistics:")
        print(f"   • Transactions this week: {weekly_tx}")
        print(f"   • Value this week: R{weekly_value:.2f}")
        print(f"   • Total villages: {villages}")
        print(f"   • Total marketplace items: {total_items}")
        print(f"🔒 Next backup: {now + timedelta(weeks=1):%Y-%m-%d}")
        print("")
        print("💡 To automate: Add to crontab: 0 0 * * 0 python3 /path/to/weekly_backup.py")
        
        return True
        
    except Exception as e:
        print(f"❌ Backup failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = weekly_backup()
    sys.exit(0 if success else 1)
