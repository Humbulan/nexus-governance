#! /usr/bin/env python3
#!/usr/bin/env python3
"""
🏛️ GAUTENG POWER GRID - TRIPLE NODE MONITORING
Monitors Sandton, Midrand, Kempton simultaneously
"""
import json
import sys
from datetime import datetime
import os

NODES_FILE = os.path.expanduser('~/humbu_community_nexus/gauteng_nodes.json')
LOG_FILE = os.path.expanduser('~/logs/industrial_alerts.log')

# Default nodes with 2026 targets
DEFAULT_NODES = {
    "SANDTON TECH": {
        "current": 185400.00,
        "target": 250000.00,
        "type": "Enterprise AI",
        "strategy": "Accelerate for R250k Milestone",
        "weekly_growth": 12500.00
    },
    "MIDRAND LOGISTICS": {
        "current": 124200.00,
        "target": 200000.00,
        "type": "Bulk Logistics",
        "strategy": "Link to Village Delivery Ranks",
        "weekly_growth": 8500.00
    },
    "KEMPTON MANUFACTURING": {
        "current": 98130.15,
        "target": 150000.00,
        "type": "Predictive Manufacturing",
        "strategy": "Stability for Industrial Backing",
        "weekly_growth": 7200.00
    }
}

def load_nodes():
    """Load or initialize node data"""
    if os.path.exists(NODES_FILE):
        with open(NODES_FILE, 'r') as f:
            return json.load(f)
    else:
        with open(NODES_FILE, 'w') as f:
            json.dump(DEFAULT_NODES, f, indent=2)
        return DEFAULT_NODES

def save_nodes(nodes):
    """Save node data"""
    with open(NODES_FILE, 'w') as f:
        json.dump(nodes, f, indent=2)

def update_node(node_name, amount):
    """Update a node's current value"""
    nodes = load_nodes()
    if node_name in nodes:
        nodes[node_name]["current"] += amount
        save_nodes(nodes)
        log_alert(f"💰 {node_name}: +R{amount:,.2f} (Total: R{nodes[node_name]['current']:,.2f})")
        return True
    return False

def check_all_nodes():
    """Display current node status"""
    nodes = load_nodes()
    
    print("\n" + "="*60)
    print("🏛️ GAUTENG INDUSTRIAL NODE PULSE")
    print("="*60)
    print(f"📅 Imperial Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("")
    
    total_current = 0
    total_target = 0
    
    print(f"{'NODE':20} {'CURRENT':>12} {'TARGET':>12} {'PROGRESS':>12} {'STATUS':>10}")
    print("-"*70)
    
    for name, data in nodes.items():
        current = data["current"]
        target = data["target"]
        percent = (current / target) * 100 if target > 0 else 0
        
        total_current += current
        total_target += target
        
        if current >= target:
            status = "💎 HIT!"
            progress_bar = "▓▓▓▓▓▓▓▓▓▓"
        else:
            status = f"{percent:.1f}%"
            filled = int(percent / 10)
            progress_bar = "▓" * filled + "░" * (10 - filled)
        
        print(f"{name:20} R{current:>11,.2f} R{target:>11,.2f} {progress_bar:>12} {status:>10}")
    
    print("-"*70)
    total_percent = (total_current / total_target) * 100 if total_target > 0 else 0
    print(f"{'TOTAL POWER GRID':20} R{total_current:>11,.2f} R{total_target:>11,.2f} {total_percent:>12.1f}%")
    print("="*60)
    
    # Strategy summary
    print("\n🎯 NODE STRATEGIES:")
    print("-"*60)
    for name, data in nodes.items():
        print(f"• {name}:")
        print(f"  Type: {data['type']}")
        print(f"  Strategy: {data['strategy']}")
        print(f"  Weekly Growth: R{data['weekly_growth']:,.2f}")
    
    # Save to log
    log_alert(f"Power Grid Check: R{total_current:,.2f}/{total_target:,.2f} ({total_percent:.1f}%)")

def log_alert(message):
    """Log industrial alerts"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}\n"
    
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)
    
    print(f"📝 Logged: {message}")

def weekly_briefing():
    """Generate weekly CEO briefing"""
    nodes = load_nodes()
    total_current = sum(n["current"] for n in nodes.values())
    total_target = sum(n["target"] for n in nodes.values())
    total_percent = (total_current / total_target) * 100 if total_target > 0 else 0
    
    briefing = f"""
🏛️ GAUTENG POWER GRID - WEEKLY CEO BRIEFING
===========================================
Report Date: {datetime.now().strftime('%Y-%m-%d')}
Imperial Timeline: 17.3 months to R5,000,000.00

📊 OVERALL STATUS:
• Total Current Yield: R{total_current:,.2f}
• Total Target: R{total_target:,.2f}
• Overall Progress: {total_percent:.1f}%

🔧 NODE PERFORMANCE:
"""
    
    for name, data in nodes.items():
        percent = (data["current"] / data["target"]) * 100 if data["target"] > 0 else 0
        briefing += f"\n• {name}:"
        briefing += f"\n  Current: R{data['current']:,.2f}"
        briefing += f"\n  Target: R{data['target']:,.2f}"
        briefing += f"\n  Progress: {percent:.1f}%"
        briefing += f"\n  Weekly Growth: R{data['weekly_growth']:,.2f}"
        briefing += f"\n  Strategy: {data['strategy']}"
    
    briefing += f"""

🎯 RECOMMENDED ACTIONS:
1. Sandton: Focus on AI enterprise contracts
2. Midrand: Expand logistics partnerships
3. Kempton: Stabilize manufacturing pipeline

📈 PROJECTED NEXT WEEK:
• Total Growth: R{sum(n['weekly_growth'] for n in nodes.values()):,.2f}
• New Total: R{total_current + sum(n['weekly_growth'] for n in nodes.values()):,.2f}
• New Progress: {((total_current + sum(n['weekly_growth'] for n in nodes.values())) / total_target * 100):.1f}%

🏛️ IMPERIAL MANDATE: TRACK. EXPAND. DELIVER.
"""
    
    # Save briefing
    briefing_file = f"~/humbu_community_nexus/ceo_briefing_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(os.path.expanduser(briefing_file), 'w') as f:
        f.write(briefing)
    
    print(briefing)
    print(f"📄 Briefing saved to: {briefing_file}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "check":
            check_all_nodes()
        elif command == "briefing":
            weekly_briefing()
        elif command == "update" and len(sys.argv) >= 4:
            node = sys.argv[2]
            amount = float(sys.argv[3])
            update_node(node, amount)
            check_all_nodes()
        elif command == "add":
            # Interactive node addition
            print("Enter new node details:")
            name = input("Node name: ")
            current = float(input("Current amount: R"))
            target = float(input("Target amount: R"))
            node_type = input("Node type: ")
            strategy = input("Strategy: ")
            
            nodes = load_nodes()
            nodes[name] = {
                "current": current,
                "target": target,
                "type": node_type,
                "strategy": strategy,
                "weekly_growth": 0
            }
            save_nodes(nodes)
            print(f"✅ Node '{name}' added to Power Grid!")
        else:
            print("❌ Unknown command")
            print("Available commands: check, briefing, update [node] [amount], add")
    else:
        check_all_nodes()
