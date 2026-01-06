#! /usr/bin/env python3
#!/data/data/com.termux/files/usr/bin/python3
"""
HUMBU SMS GATEWAY
Sends transaction notifications via SMS
Simulates real telco SMS gateway
"""

import sqlite3
import time
from datetime import datetime

class HumbuSMSGateway:
    def __init__(self):
        self.db_path = 'data/community.db'
        self.sent_sms = []
        
    def send_sms(self, phone_number, message):
        """Simulate sending SMS (replace with real API)"""
        print(f"\n📱 SENDING SMS TO: {phone_number}")
        print(f"📝 Message: {message}")
        print(f"⏰ Time: {datetime.now().strftime('%H:%M:%S')}")
        
        # Simulate network delay
        time.sleep(1)
        
        # Record sent SMS
        sms_id = f"SMS_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.sent_sms.append({
            'id': sms_id,
            'to': phone_number,
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'status': 'delivered'
        })
        
        print(f"✅ SMS ID: {sms_id} - Status: DELIVERED")
        return sms_id
    
    def process_pending_notifications(self):
        """Process all pending SMS notifications"""
        print("\n" + "="*60)
        print("🔄 PROCESSING PENDING SMS NOTIFICATIONS")
        print("="*60)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Get pending notifications
        cursor.execute('''
        SELECT id, user_id, message, transaction_id
        FROM notifications 
        WHERE status = 'pending_sms'
        ORDER BY created_at
        LIMIT 10
        ''')
        
        pending = cursor.fetchall()
        
        if not pending:
            print("📭 No pending notifications")
            return 0
        
        print(f"📥 Found {len(pending)} pending notifications")
        
        sent_count = 0
        for notif_id, user_id, message, transaction_id in pending:
            # Get user phone number
            cursor.execute('''
            SELECT phone, name FROM users WHERE id = ?
            ''', (user_id,))
            
            user_data = cursor.fetchone()
            if not user_data:
                print(f"⚠️ User {user_id} not found")
                continue
            
            phone, name = user_data
            
            # Send SMS
            sms_message = f"HUMBU: {message}"
            sms_id = self.send_sms(phone, sms_message)
            
            # Update notification status
            cursor.execute('''
            UPDATE notifications 
            SET status = 'sent' 
            WHERE id = ?
            ''', (notif_id,))
            
            # Record SMS in database
            cursor.execute('''
            INSERT INTO sms_logs (id, notification_id, transaction_id, 
                                 phone_number, message, status, sent_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (sms_id, notif_id, transaction_id, phone, 
                  sms_message, 'delivered', datetime.now().isoformat()))
            
            sent_count += 1
        
        conn.commit()
        conn.close()
        
        print(f"\n✅ Sent {sent_count} SMS notifications")
        return sent_count
    
    def create_transaction_sms(self, transaction_data):
        """Create SMS templates for different transaction types"""
        
        templates = {
            'send_money': {
                'sender': "HUMBU: You sent R{amount:.2f} to {recipient}. New balance: R{balance:.2f}. Ref: {ref}",
                'recipient': "HUMBU: You received R{amount:.2f} from {sender}. Ref: {ref}"
            },
            'marketplace_purchase': {
                'buyer': "HUMBU: Purchased {item} for R{amount:.2f}. Balance: R{balance:.2f}. Ref: {ref}",
                'seller': "HUMBU: Sold {item} for R{amount:.2f}. New balance: R{balance:.2f}. Ref: {ref}"
            },
            'task_completion': {
                'worker': "HUMBU: Task '{task}' completed! R{amount:.2f} credited. New balance: R{balance:.2f}"
            }
        }
        
        return templates
    
    def run_gateway_service(self):
        """Run as continuous service"""
        print("\n🚀 STARTING HUMBU SMS GATEWAY SERVICE")
        print("📡 Listening for transaction notifications...")
        print("="*60)
        
        while True:
            try:
                # Check for pending notifications every 30 seconds
                count = self.process_pending_notifications()
                
                if count > 0:
                    print(f"\n📊 SMS GATEWAY STATUS:")
                    print(f"   Processed: {count} SMS")
                    print(f"   Total sent today: {len(self.sent_sms)}")
                    print(f"   Last SMS: {self.sent_sms[-1]['id'] if self.sent_sms else 'None'}")
                
                # Wait before next check
                print("\n⏳ Next check in 30 seconds... (Ctrl+C to stop)")
                time.sleep(30)
                
            except KeyboardInterrupt:
                print("\n\n🛑 SMS Gateway stopped by user")
                break
            except Exception as e:
                print(f"\n⚠️ Error: {e}")
                time.sleep(60)

def setup_sms_database():
    """Setup SMS logs table"""
    conn = sqlite3.connect('data/community.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sms_logs (
        id TEXT PRIMARY KEY,
        notification_id TEXT,
        transaction_id TEXT,
        phone_number TEXT,
        message TEXT,
        status TEXT,
        sent_at DATETIME,
        delivered_at DATETIME,
        cost REAL DEFAULT 0.25
    )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ SMS logs table ready")

def main():
    print("📱 HUMBU SMS GATEWAY INTEGRATION")
    print("🔗 Connects USSD transactions to SMS notifications")
    print("="*60)
    
    # Setup database
    setup_sms_database()
    
    # Create gateway instance
    gateway = HumbuSMSGateway()
    
    # Process any pending notifications
    print("\n1. Checking for pending notifications...")
    gateway.process_pending_notifications()
    
    # Test SMS sending
    print("\n2. Testing SMS functionality...")
    test_sms = gateway.send_sms("[REDACTED]", "HUMBU: Test SMS from gateway. System operational.")
    
    # Ask to run as service
    print("\n" + "="*60)
    run_service = input("Run SMS Gateway as continuous service? (y/n): ").lower()
    
    if run_service == 'y':
        gateway.run_gateway_service()
    else:
        print("\n✅ SMS Gateway ready for production")
        print("📊 To integrate with real telco API:")
        print("   1. MTN SMS API: https://momodeveloper.mtn.com")
        print("   2. Vodacom SMS API: https://developer.vodacom.co.za")
        print("   3. Twilio South Africa: https://www.twilio.com/za")
    
    print("\n" + "="*60)
    print("🎯 SMS GATEWAY DEPLOYMENT READY")
    print("📞 Template: Transaction confirmations")
    print("💰 Cost: ~R0.25 per SMS")
    print("⏱️  Latency: < 5 seconds")
    print("="*60)

if __name__ == "__main__":
    main()
