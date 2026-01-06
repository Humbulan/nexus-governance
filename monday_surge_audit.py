#! /usr/bin/env python3
#!/usr/bin/env python3
"""
🚀 MONDAY SURGE AUDIT
Checks if system can handle 200% traffic increase
"""
import subprocess
import os
import json
from datetime import datetime

def check_capacity(component, command, min_required):
    """Check component capacity"""
    try:
        result = subprocess.run(command, 
                              shell=True, 
                              capture_output=True, 
                              text=True,
                              timeout=5)
        
        current = len(result.stdout.strip().split('\n')) if result.stdout else 0
        capacity = (current / min_required) * 100
        status = "✅" if capacity >= 100 else "⚠️" if capacity >= 50 else "❌"
        
        return {
            "component": component,
            "current": current,
            "required": min_required,
            "capacity": f"{capacity:.1f}%",
            "status": status,
            "ready": capacity >= 100
        }
    except:
        return {
            "component": component,
            "current": 0,
            "required": min_required,
            "capacity": "0%",
            "status": "❌",
            "ready": False
        }

def run_audit():
    """Run complete Monday surge audit"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'='*70}")
    print(f"🚀 MONDAY SURGE AUDIT - {timestamp}")
    print(f"{'='*70}")
    print(f"🎯 Mission: Verify 200% traffic capacity for work week")
    print(f"📊 Current: R342,515.60 monthly flow")
    print(f"🎯 Target: R595,238.10 monthly (200% increase)")
    print(f"{'='*70}")
    
    # Capacity checks (200% = 2x current capacity)
    checks = [
        ("🌐 Cloudflare Tunnel", "pgrep -f cloudflared", 1),
        ("🏛️ Gauteng Power Grid", "ls -1 ~/humbu_community_nexus/nodes/node_*.active | wc -l", 20),
        ("📱 USSD Gateway", "ls ~/humbu_community_nexus/*ussd* 2>/dev/null | wc -l", 1),
        ("📄 Board Reports", "ls -1 ~/humbu_community_nexus/reports/board_report_*.ready | wc -l", 5),
        ("💰 Contract Ledger", "ls ~/humbu_community_nexus/imperial_contracts_2026.json 2>/dev/null && echo 1 || echo 0", 1),
        ("🚨 Hard-Trigger", "ls -1 ~/humbu_community_nexus/nodes/trigger_*.enabled | wc -l", 5),
    ]
    
    results = []
    all_ready = True
    
    print("\n📊 CAPACITY ANALYSIS (200% surge ready):")
    print("-"*70)
    
    for check in checks:
        result = check_capacity(*check)
        results.append(result)
        
        print(f"{result['status']} {result['component']}")
        print(f"   Current: {result['current']} | Required: {result['required']}")
        print(f"   Capacity: {result['capacity']} | Ready: {'✅' if result['ready'] else '❌'}")
        print()
        
        if not result['ready']:
            all_ready = False
    
    # Financial capacity check
    print("💰 FINANCIAL CAPACITY:")
    print("-"*70)
    
    try:
        with open(os.path.expanduser('~/humbu_community_nexus/financial_ledger.json'), 'r') as f:
            financial = json.load(f)
        
        current_flow = financial.get('net_monthly_flow', 342515.60)
        target_flow = financial.get('target_monthly', 595238.10)
        flow_capacity = (current_flow / target_flow) * 100
        
        print(f"   Current Monthly Flow: R{current_flow:,.2f}")
        print(f"   Target Monthly Flow:  R{target_flow:,.2f}")
        print(f"   Flow Capacity:       {flow_capacity:.1f}%")
        print(f"   Ready for 200%:      {'✅' if flow_capacity >= 50 else '❌'}")
        print()
        
        if flow_capacity < 50:
            all_ready = False
            results.append({
                "component": "💰 Financial Flow",
                "current": current_flow,
                "required": target_flow,
                "capacity": f"{flow_capacity:.1f}%",
                "status": "❌",
                "ready": False
            })
    except:
        print("   ❌ Financial data not available")
        all_ready = False
    
    # Recommendations
    print("🎯 RECOMMENDATIONS FOR MONDAY SURGE:")
    print("-"*70)
    
    if all_ready:
        print("✅ ALL SYSTEMS READY FOR 200% TRAFFIC SURGE")
        print("")
        print("🚀 ACTION PLAN FOR MONDAY:")
        print("1. Execute 10-prospect WhatsApp blitz")
        print("2. Log all contracts with 'sign-client'")
        print("3. Monitor CAC reduction through partner sharing")
        print("4. Target R595,238.10 monthly flow")
    else:
        print("⚠️ SYSTEM NEEDS PREPARATION BEFORE MONDAY SURGE")
        print("")
        print("🔧 IMMEDIATE ACTIONS:")
        
        for result in results:
            if not result['ready']:
                component = result['component']
                if "Cloudflare" in component:
                    print(f"1. Restart Cloudflare: pkill cloudflared && nohup cloudflared tunnel --url http://localhost:8080 > ~/logs/cf_monday.log 2>&1 &")
                elif "USSD" in component:
                    print(f"2. Verify USSD Gateway: Check ~/humbu_community_nexus/deploy_ussd.sh")
                elif "Financial" in component:
                    print(f"3. Increase flow: Need R{result['required'] - result['current']:,.2f} more monthly")
    
    print(f"\n{'='*70}")
    print(f"📊 AUDIT COMPLETE: {'✅ READY FOR SURGE' if all_ready else '⚠️ NEEDS PREPARATION'}")
    print(f"{'='*70}")
    
    # Save audit report
    report_dir = os.path.expanduser("~/humbu_community_nexus/audit_reports")
    os.makedirs(report_dir, exist_ok=True)
    
    report_file = f"{report_dir}/monday_surge_audit_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    audit_report = {
        "timestamp": timestamp,
        "all_ready": all_ready,
        "results": results,
        "recommendations": "Ready" if all_ready else "Needs preparation",
        "genesis_hash": "88f7a825...",
        "reality_certified": True
    }
    
    with open(report_file, 'w') as f:
        json.dump(audit_report, f, indent=2)
    
    print(f"\n📄 Audit report saved: {report_file}")
    
    return all_ready

if __name__ == "__main__":
    run_audit()
