#! /usr/bin/env python3
#!/usr/bin/env python3
"""
IMPERIAL LEAD TRACKER - 2026 LAUNCH CAMPAIGN
Tracks all responses from Digital Blast campaign
"""
import json
import csv
from datetime import datetime
import os

LEADS_FILE = os.path.expanduser('~/humbu_community_nexus/imperial_leads_2026.json')
CSV_FILE = os.path.expanduser('~/humbu_community_nexus/leads_export.csv')

def init_leads():
    """Initialize leads database"""
    if not os.path.exists(LEADS_FILE):
        with open(LEADS_FILE, 'w') as f:
            json.dump([], f)
        print("✅ Imperial Leads Database initialized")
    else:
        print("📊 Existing leads database loaded")

def add_lead(name, platform, response_type, contact_info=""):
    """Add a new lead from campaign"""
    with open(LEADS_FILE, 'r') as f:
        leads = json.load(f)
    
    lead = {
        "id": len(leads) + 1,
        "name": name,
        "platform": platform,
        "response_type": response_type,
        "contact_info": contact_info,
        "timestamp": datetime.now().isoformat(),
        "status": "new",
        "follow_up": "pending",
        "notes": ""
    }
    
    leads.append(lead)
    
    with open(LEADS_FILE, 'w') as f:
        json.dump(leads, f, indent=2)
    
    print(f"🎯 LEAD CAPTURED: {name} via {platform} ({response_type})")
    return lead

def export_to_csv():
    """Export leads to CSV for calling"""
    with open(LEADS_FILE, 'r') as f:
        leads = json.load(f)
    
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'id', 'name', 'platform', 'response_type', 
            'contact_info', 'timestamp', 'status', 'follow_up'
        ])
        writer.writeheader()
        writer.writerows(leads)
    
    print(f"📈 Exported {len(leads)} leads to {CSV_FILE}")
    return CSV_FILE

def show_dashboard():
    """Show leads dashboard"""
    with open(LEADS_FILE, 'r') as f:
        leads = json.load(f)
    
    print("\n" + "="*60)
    print("🎯 IMPERIAL LEAD TRACKER - 2026 LAUNCH CAMPAIGN")
    print("="*60)
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"👥 Total Leads: {len(leads)}")
    print(f"📊 New Today: {sum(1 for l in leads if l['timestamp'].startswith(datetime.now().strftime('%Y-%m-%d')))}")
    print("\n📱 By Platform:")
    platforms = {}
    for lead in leads:
        platforms[lead['platform']] = platforms.get(lead['platform'], 0) + 1
    
    for platform, count in platforms.items():
        print(f"  • {platform}: {count} leads")
    
    print("\n🎯 Priority Follow-ups:")
    new_leads = [l for l in leads if l['status'] == 'new']
    for lead in new_leads[:5]:  # Show top 5
        print(f"  {lead['id']}. {lead['name']} - {lead['platform']} ({lead['response_type']})")
    
    print("\n💡 Commands:")
    print("  python3 lead_tracker.py add 'Name' 'Platform' 'Response'")
    print("  python3 lead_tracker.py dashboard")
    print("  python3 lead_tracker.py export")
    print("="*60)

if __name__ == "__main__":
    import sys
    
    init_leads()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "add" and len(sys.argv) >= 4:
            name = sys.argv[2]
            platform = sys.argv[3]
            response = sys.argv[4] if len(sys.argv) > 4 else "IMPERIAL"
            contact = sys.argv[5] if len(sys.argv) > 5 else ""
            add_lead(name, platform, response, contact)
        
        elif command == "dashboard":
            show_dashboard()
        
        elif command == "export":
            export_to_csv()
        
        else:
            print("❌ Unknown command")
            show_dashboard()
    else:
        show_dashboard()
