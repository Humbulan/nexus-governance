#! /usr/bin/env python3
#!/usr/bin/env python3
"""
🏛️ IMPERIAL CONTRACT LEDGER
Logs all client contracts for 2026 financial tracking
"""
import json
import os
import sys
from datetime import datetime
import subprocess

CONTRACTS_FILE = os.path.expanduser('~/humbu_community_nexus/imperial_contracts_2026.json')
FINANCIAL_SUMMARY = os.path.expanduser('~/humbu_community_nexus/financial_ledger.json')
TIERS = {
    "TIER_1": {"name": "Village Basic", "value": 1500, "description": "40-village access"},
    "TIER_2": {"name": "Logistics Pro", "value": 5000, "description": "Gauteng + Village"},
    "TIER_3": {"name": "Industrial Elite", "value": 15000, "description": "Full Imperial Suite"}
}

def init_files():
    """Initialize contract and financial files"""
    if not os.path.exists(CONTRACTS_FILE):
        with open(CONTRACTS_FILE, 'w') as f:
            json.dump([], f)
    
    if not os.path.exists(FINANCIAL_SUMMARY):
        base_financial = {
            "net_monthly_flow": 342515.60,
            "urban_cac": 74151.07,
            "target_monthly": 595238.10,
            "months_to_5m": 14.6,
            "total_contracts": 0,
            "total_value": 0,
            "last_updated": datetime.now().isoformat()
        }
        with open(FINANCIAL_SUMMARY, 'w') as f:
            json.dump(base_financial, f, indent=2)

def log_contract(client_name, tier_type, custom_value=None):
    """Log a new contract to the ledger"""
    init_files()
    
    # Get tier value
    if tier_type in TIERS:
        tier_value = TIERS[tier_type]["value"]
        tier_name = TIERS[tier_type]["name"]
    else:
        try:
            tier_value = float(custom_value)
            tier_name = "Custom Tier"
        except:
            print("❌ Invalid tier value")
            return False
    
    contract = {
        "id": f"CONTRACT_{datetime.now().strftime('%Y%m%d%H%M%S')}",
        "timestamp": datetime.now().isoformat(),
        "client": client_name,
        "tier": tier_name,
        "value": tier_value,
        "status": "SIGNED",
        "payment_status": "PENDING",
        "cac_impact": tier_value * 0.25,  # 25% CAC reduction through partner sharing
        "notes": ""
    }
    
    # Load existing contracts
    with open(CONTRACTS_FILE, 'r') as f:
        contracts = json.load(f)
    
    contracts.append(contract)
    
    # Save updated contracts
    with open(CONTRACTS_FILE, 'w') as f:
        json.dump(contracts, f, indent=2)
    
    # Update financial summary
    update_financial_summary(contracts)
    
    # Send notification
    send_contract_alert(contract)
    
    print(f"\n{'='*60}")
    print(f"🏛️  IMPERIAL CONTRACT SECURED")
    print(f"{'='*60}")
    print(f"📝 Client: {client_name}")
    print(f"💰 Value: R{tier_value:,.2f}")
    print(f"🎯 Tier: {tier_name}")
    print(f"📅 Signed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📊 CAC Impact: R{contract['cac_impact']:,.2f} (25% reduction)")
    print(f"{'='*60}")
    
    return True

def update_financial_summary(contracts):
    """Update financial summary with new contracts"""
    total_contracts = len(contracts)
    total_value = sum(c["value"] for c in contracts)
    
    with open(FINANCIAL_SUMMARY, 'r') as f:
        financial = json.load(f)
    
    # Update values
    financial["total_contracts"] = total_contracts
    financial["total_value"] = total_value
    financial["net_monthly_flow"] = 342515.60 + (total_value * 0.8)  # 80% conversion to net
    financial["last_updated"] = datetime.now().isoformat()
    
    # Calculate new timeline
    remaining_to_5m = 5000000 - (financial["net_monthly_flow"] * financial["months_to_5m"])
    if financial["net_monthly_flow"] > 0:
        financial["months_to_5m"] = remaining_to_5m / financial["net_monthly_flow"]
    
    with open(FINANCIAL_SUMMARY, 'w') as f:
        json.dump(financial, f, indent=2)

def send_contract_alert(contract):
    """Send Android notification for new contract"""
    try:
        title = f"🏛️ CONTRACT: {contract['client']}"
        content = f"R{contract['value']:,.2f} - {contract['tier']}"
        
        subprocess.run([
            "termux-notification",
            "--title", title,
            "--content", content,
            "--priority", "high",
            "--led-color", "00FF00"
        ], capture_output=True)
    except:
        pass  # Notification optional

def show_financial_dashboard():
    """Display financial dashboard"""
    init_files()
    
    with open(FINANCIAL_SUMMARY, 'r') as f:
        financial = json.load(f)
    
    with open(CONTRACTS_FILE, 'r') as f:
        contracts = json.load(f)
    
    print(f"\n{'='*70}")
    print(f"🏛️  IMPERIAL FINANCIAL LEDGER - 2026")
    print(f"{'='*70}")
    print(f"📅 Last Updated: {financial['last_updated']}")
    print(f"")
    
    print(f"📊 FINANCIAL METRICS:")
    print(f"  • Net Monthly Flow:    R{financial['net_monthly_flow']:,.2f}")
    print(f"  • Urban CAC:           R{financial['urban_cac']:,.2f}")
    print(f"  • Target Monthly:      R{financial['target_monthly']:,.2f}")
    print(f"  • Months to R5M:       {financial['months_to_5m']:.1f}")
    print(f"  • Gap to Target:       R{financial['target_monthly'] - financial['net_monthly_flow']:,.2f}")
    print(f"")
    
    print(f"📈 CONTRACT PERFORMANCE:")
    print(f"  • Total Contracts:     {financial['total_contracts']}")
    print(f"  • Total Value:         R{financial['total_value']:,.2f}")
    print(f"  • Avg. Contract Value: R{financial['total_value']/max(financial['total_contracts'],1):,.2f}")
    print(f"")
    
    # Monday Surge Strategy
    cac_reduction = financial['urban_cac'] * 0.25
    print(f"🚀 MONDAY SURGE STRATEGY:")
    print(f"  • Current CAC:         R{financial['urban_cac']:,.2f}")
    print(f"  • 25% Partner Sharing: R{cac_reduction:,.2f} reduction")
    print(f"  • New CAC:             R{financial['urban_cac'] - cac_reduction:,.2f}")
    print(f"  • Client Target:       10 prospects this week")
    print(f"")
    
    # Recent contracts
    if contracts:
        print(f"📝 RECENT CONTRACTS (last 5):")
        for contract in contracts[-5:]:
            date = contract['timestamp'].split('T')[0]
            print(f"  • {contract['client']}: R{contract['value']:,.2f} ({date})")
    
    print(f"{'='*70}")
    print(f"🎯 GENESIS HASH: 88f7a825... (Reality Certified)")
    print(f"{'='*70}")

def list_tiers():
    """List available contract tiers"""
    print(f"\n🏛️ AVAILABLE CONTRACT TIERS:")
    print(f"{'='*50}")
    for tier_id, tier_info in TIERS.items():
        print(f"{tier_id}:")
        print(f"  Name: {tier_info['name']}")
        print(f"  Value: R{tier_info['value']:,.2f}")
        print(f"  Description: {tier_info['description']}")
        print(f"  CAC Impact: R{tier_info['value'] * 0.25:,.2f} (25% reduction)")
        print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "dashboard":
            show_financial_dashboard()
        elif command == "log":
            if len(sys.argv) >= 4:
                client = sys.argv[2]
                tier = sys.argv[3]
                custom = sys.argv[4] if len(sys.argv) > 4 else None
                log_contract(client, tier, custom)
            else:
                print("❌ Usage: python3 contract_logger.py log [client] [tier] [custom_value]")
        elif command == "tiers":
            list_tiers()
        elif command == "add":
            # Interactive mode
            print("\n🏛️ IMPERIAL CONTRACT LOGGER")
            print("="*40)
            
            list_tiers()
            
            client = input("\nEnter Client Name: ")
            print("\nAvailable Tiers: TIER_1 (R1,500), TIER_2 (R5,000), TIER_3 (R15,000)")
            tier = input("Enter Tier (TIER_1/TIER_2/TIER_3/CUSTOM): ").upper()
            
            if tier == "CUSTOM":
                custom_val = input("Enter Custom Value: R")
                try:
                    value = float(custom_val)
                    log_contract(client, "CUSTOM", value)
                except:
                    print("❌ Invalid custom value")
            elif tier in TIERS:
                log_contract(client, tier)
            else:
                print("❌ Invalid tier selected")
        else:
            print("❌ Unknown command")
            print("Available: dashboard, log, tiers, add")
    else:
        # Default: show dashboard
        show_financial_dashboard()
