#! /usr/bin/env python3
#!/usr/bin/env python3
"""
🛡️ PLATFORM-FREEZE SAFETY PROTOCOL
Locks USSD Gateway if suspicious transaction detected
"""
import json
import os
from datetime import datetime

SUSPICIOUS_THRESHOLD = 50000.00  # R50K
SAFETY_LOG = os.path.expanduser('~/logs/platform_safety.log')
FREEZE_STATUS = os.path.expanduser('~/humbu_community_nexus/freeze_status.json')

def check_transaction(amount, location, node):
    """Check if transaction triggers safety protocol"""
    
    # Suspicious patterns
    suspicious_patterns = [
        amount > SUSPICIOUS_THRESHOLD,
        location not in ["Sandton", "Midrand", "Kempton", "Gauteng"],
        node not in ["SANDTON TECH", "MIDRAND LOGISTICS", "KEMPTON MANUFACTURING"]
    ]
    
    if any(suspicious_patterns):
        trigger_freeze(amount, location, node)
        return False  # Transaction blocked
    else:
        log_safety(f"Transaction approved: R{amount:,.2f} at {location} ({node})")
        return True  # Transaction approved

def trigger_freeze(amount, location, node):
    """Activate platform freeze"""
    freeze_data = {
        "timestamp": datetime.now().isoformat(),
        "amount": amount,
        "location": location,
        "node": node,
        "reason": "Suspicious transaction pattern",
        "status": "FROZEN"
    }
    
    # Save freeze status
    with open(FREEZE_STATUS, 'w') as f:
        json.dump(freeze_data, f, indent=2)
    
    # Log the freeze
    log_safety(f"🚨 PLATFORM FREEZE ACTIVATED: R{amount:,.2f} at {location}")
    log_safety(f"   Node: {node}")
    log_safety(f"   Reason: Exceeds R{SUSPICIOUS_THRESHOLD:,.2f} or outside Gauteng")
    
    # Send alert
    try:
        import subprocess
        subprocess.run([
            "termux-notification",
            "--title", "🛡️ PLATFORM FREEZE ACTIVATED",
            "--content", f"Suspicious: R{amount:,.2f} at {location}",
            "--priority", "max",
            "--led-color", "FF0000"
        ])
    except:
        pass
    
    print("🚨 PLATFORM FREEZE ACTIVATED!")
    print(f"   Transaction: R{amount:,.2f} at {location}")
    print(f"   USSD Gateway temporarily locked")
    print(f"   Check {FREEZE_STATUS} for details")

def release_freeze():
    """Release platform freeze"""
    if os.path.exists(FREEZE_STATUS):
        os.remove(FREEZE_STATUS)
        log_safety("✅ Platform freeze released")
        print("✅ Platform freeze released")
        return True
    else:
        print("⚠️  No active freeze found")
        return False

def check_freeze_status():
    """Check current freeze status"""
    if os.path.exists(FREEZE_STATUS):
        with open(FREEZE_STATUS, 'r') as f:
            status = json.load(f)
        
        print("🛡️ PLATFORM FREEZE STATUS:")
        print(f"   Status: {status['status']}")
        print(f"   Since: {status['timestamp']}")
        print(f"   Reason: {status['reason']}")
        print(f"   Amount: R{status['amount']:,.2f}")
        print(f"   Location: {status['location']}")
        return True
    else:
        print("✅ Platform: UNFROZEN (Operational)")
        return False

def log_safety(message):
    """Log safety events"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}\n"
    
    with open(SAFETY_LOG, 'a') as f:
        f.write(log_entry)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "check":
            amount = float(sys.argv[2]) if len(sys.argv) > 2 else 0
            location = sys.argv[3] if len(sys.argv) > 3 else "Unknown"
            node = sys.argv[4] if len(sys.argv) > 4 else "Unknown"
            
            if check_transaction(amount, location, node):
                print(f"✅ Transaction approved: R{amount:,.2f}")
            else:
                print(f"❌ Transaction blocked: R{amount:,.2f}")
        
        elif command == "status":
            check_freeze_status()
        
        elif command == "release":
            release_freeze()
        
        elif command == "test":
            # Test suspicious transaction
            print("🔍 Testing suspicious transaction...")
            check_transaction(75000.00, "Cape Town", "UNKNOWN_NODE")
        
        else:
            print("❌ Unknown command")
            print("Available: check [amount] [location] [node], status, release, test")
    else:
        check_freeze_status()
