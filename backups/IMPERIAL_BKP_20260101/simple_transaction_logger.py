#!/data/data/com.termux/files/usr/bin/python3
"""
SIMPLE TRANSACTION LOGGER
Tracks R50,000 monthly goal
"""

import sqlite3
from datetime import datetime
import csv

def setup_logger():
    """Setup transaction logging"""
    conn = sqlite3.connect('data/community.db')
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transaction_logs (
        id TEXT PRIMARY KEY,
        date TEXT,
        amount REAL,
        user_id TEXT,
        phone TEXT,
        status TEXT,
        reference TEXT,
        provider TEXT DEFAULT 'mtn_momo'
    )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Transaction logger ready")

def log_transaction(amount, phone, reference, status="success"):
    """Log a transaction"""
    conn = sqlite3.connect('data/community.db')
    cursor = conn.cursor()
    
    transaction_id = f"TXN_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    cursor.execute('''
    INSERT INTO transaction_logs (id, date, amount, phone, status, reference)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        transaction_id,
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        amount,
        phone,
        status,
        reference
    ))
    
    conn.commit()
    conn.close()
    
    print(f"✅ Transaction logged: {transaction_id}")
    print(f"   Amount: R{amount}")
    print(f"   Phone: {phone}")
    print(f"   Status: {status}")
    
    return transaction_id

def get_monthly_total():
    """Get current month's total"""
    conn = sqlite3.connect('data/community.db')
    cursor = conn.cursor()
    
    current_month = datetime.now().strftime('%Y-%m')
    
    cursor.execute('''
    SELECT SUM(amount) as total, COUNT(*) as count
    FROM transaction_logs 
    WHERE date LIKE ? AND status = 'success'
    ''', (f'{current_month}%',))
    
    result = cursor.fetchone()
    total = result[0] if result[0] else 0
    count = result[1] if result[1] else 0
    
    conn.close()
    
    return total, count

def show_progress():
    """Show progress toward R50,000 goal"""
    total, count = get_monthly_total()
    goal = 50000
    progress = (total / goal) * 100
    
    print("\n📊 MONTHLY PROGRESS")
    print("==================")
    print(f"Goal: R{goal:,.2f}")
    print(f"Current: R{total:,.2f}")
    print(f"Progress: {progress:.1f}%")
    print(f"Transactions: {count}")
    print(f"Remaining: R{goal - total:,.2f}")
    
    if progress >= 100:
        print("🎉 GOAL ACHIEVED!")
    elif progress >= 75:
        print("🚀 Almost there!")
    elif progress >= 50:
        print("👍 Good progress!")
    else:
        print("📈 Keep going!")

def main():
    print("💰 HUMBU TRANSACTION LOGGER")
    print("===========================")
    
    # Setup database
    setup_logger()
    
    # Show current progress
    show_progress()
    
    # Test logging
    print("\n🧪 Testing logger...")
    log_transaction(
        amount=25.00,
        phone="072 123 4567",
        reference="test_log_001",
        status="success"
    )
    
    # Show updated progress
    show_progress()
    
    print("\n✅ Logger ready for production!")
    print("📈 Monthly goal: R50,000")
    print("👥 308 users in Limpopo")
    print("🌍 15 villages covered")

if __name__ == "__main__":
    main()
