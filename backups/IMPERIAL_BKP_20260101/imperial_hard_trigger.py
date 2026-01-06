#!/usr/bin/env python3
"""
🚨 IMPERIAL HARD-TRIGGER PROTOCOL
Active notification system for R500K milestone
Bypasses silent mode - uses Android system notifications
"""
import json
import subprocess
import sys
import os
from datetime import datetime

# Configuration
HARD_THRESHOLD = 500000.00
NODES_FILE = os.path.expanduser('~/humbu_community_nexus/gauteng_nodes.json')
LOG_FILE = os.path.expanduser('~/logs/hard_trigger.log')
ALERT_HISTORY = os.path.expanduser('~/humbu_community_nexus/alert_history.json')

def get_total_grid():
    """Calculate total from all Gauteng nodes"""
    try:
        with open(NODES_FILE, 'r') as f:
            nodes = json.load(f)
        total = sum(node["current"] for node in nodes.values())
        return total
    except:
        # Fallback to default if file doesn't exist
        return 412730.15  # Default from latest report

def log_alert(message, level="INFO"):
    """Log alert events"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)
    
    print(f"📝 {level}: {message}")

def send_hard_notification(title, content, priority="max", led_color="00FF00"):
    """Send Android system notification"""
    try:
        cmd = [
            "termux-notification",
            "--title", title,
            "--content", content,
            "--priority", priority,
            "--led-color", led_color,
            "--vibrate", "1000,1000,1000,1000",
            "--sound"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            return True
        else:
            print(f"⚠️  Notification failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"⚠️  Termux-API not available: {e}")
        return False

def trigger_check():
    """Check if threshold is reached and trigger alert"""
    current_total = get_total_grid()
    remaining = HARD_THRESHOLD - current_total
    
    print(f"🏛️ IMPERIAL HARD-TRIGGER STATUS")
    print("="*50)
    print(f"📊 Current Grid Total: R{current_total:,.2f}")
    print(f"🎯 Hard Threshold: R{HARD_THRESHOLD:,.2f}")
    
    if current_total >= HARD_THRESHOLD:
        # THRESHOLD BREACHED - HARD ALERT!
        title = "🏛️ IMPERIAL MILESTONE REACHED! 💎"
        content = f"GAUTENG POWER GRID HAS BREACHED R{current_total:,.2f}!"
        
        print(f"🚨 CRITICAL: Threshold breached by R{current_total - HARD_THRESHOLD:,.2f}")
        print(f"📢 Dispatching hard alert...")
        
        # Send notification
        if send_hard_notification(title, content):
            print("✅ Hard alert dispatched to Android system")
            log_alert(f"HARD-TRIGGER ACTIVATED: R{current_total:,.2f} >= R{HARD_THRESHOLD:,.2f}", "CRITICAL")
            
            # Record in alert history
            alert_data = {
                "timestamp": datetime.now().isoformat(),
                "total": current_total,
                "threshold": HARD_THRESHOLD,
                "breach_amount": current_total - HARD_THRESHOLD,
                "type": "HARD_TRIGGER"
            }
            
            try:
                with open(ALERT_HISTORY, 'r') as f:
                    history = json.load(f)
            except:
                history = []
            
            history.append(alert_data)
            
            with open(ALERT_HISTORY, 'w') as f:
                json.dump(history, f, indent=2)
            
            # Also trigger celebratory command
            print("\n🎉 CELEBRATORY COMMANDS:")
            print("   echo 'IMPERIAL VICTORY: R500K ACHIEVED!' | lolcat")
            print("   python3 ~/humbu_community_nexus/celebrate.py")
            
        else:
            print("⚠️  Alert dispatched but Termux-API may not be installed")
            log_alert(f"THRESHOLD BREACHED BUT NOTIFICATION FAILED: R{current_total:,.2f}", "WARNING")
    
    else:
        # Still below threshold
        print(f"📈 Remaining to threshold: R{remaining:,.2f}")
        
        # Calculate projected date (based on R28k/week growth)
        weekly_growth = 28000.00
        weeks_needed = remaining / weekly_growth
        days_needed = weeks_needed * 7
        
        projected_date = datetime.now().timestamp() + (days_needed * 86400)
        projected_str = datetime.fromtimestamp(projected_date).strftime('%Y-%m-%d')
        
        print(f"📅 Projected trigger date: ~{weeks_needed:.1f} weeks ({projected_str})")
        
        # Soft notification if close (within 10%)
        if remaining <= (HARD_THRESHOLD * 0.1):  # Within 10%
            title = "🏛️ IMPERIAL THRESHOLD APPROACHING"
            content = f"Only R{remaining:,.2f} left to R500K milestone!"
            send_hard_notification(title, content, priority="high", led_color="FFFF00")
            log_alert(f"SOFT ALERT: R{remaining:,.2f} to threshold", "INFO")
        
        log_alert(f"Monitoring: R{remaining:,.2f} to threshold", "INFO")
    
    print("="*50)

def continuous_monitor(interval_seconds=300):
    """Continuous monitoring mode (every 5 minutes)"""
    print(f"🔍 Starting continuous monitoring (every {interval_seconds} seconds)")
    print("Press Ctrl+C to stop")
    
    import time
    
    try:
        while True:
            trigger_check()
            print(f"⏳ Next check in {interval_seconds} seconds...\n")
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "monitor":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 300
            continuous_monitor(interval)
        elif command == "test":
            # Test notification
            print("🔔 Testing notification system...")
            if send_hard_notification("🏛️ TEST ALERT", "Imperial Hard-Trigger Test"):
                print("✅ Test notification sent!")
            else:
                print("❌ Test failed - check Termux:API")
        elif command == "history":
            # Show alert history
            try:
                with open(ALERT_HISTORY, 'r') as f:
                    history = json.load(f)
                
                print("📜 ALERT HISTORY:")
                for alert in history[-10:]:  # Last 10 alerts
                    print(f"  {alert['timestamp']}: R{alert['total']:,.2f} (Breach: R{alert['breach_amount']:,.2f})")
            except:
                print("No alert history found")
        else:
            print("❌ Unknown command")
            print("Available: monitor [interval], test, history")
    else:
        trigger_check()
