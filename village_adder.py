#! /usr/bin/env python3
#!/usr/bin/env python3
# 🏛️ HUMBU IMPERIAL VILLAGE ADDER
# Adds villages without starting server

import sys
import json
from datetime import datetime

def add_village_to_system(village_name, revenue_amount):
    """Add a village to the revenue system"""
    
    print(f"🏘️  ADDING VILLAGE: {village_name}")
    print(f"💰 REVENUE: R{revenue_amount:.2f}")
    
    # Simulate adding to database
    village_data = {
        "village": village_name,
        "revenue": revenue_amount,
        "timestamp": datetime.now().isoformat(),
        "status": "active",
        "region": "Limpopo" if "Malamulele" in village_name else "Gauteng"
    }
    
    # Save to a file (or database)
    try:
        # Read existing villages
        try:
            with open('village_revenues.json', 'r') as f:
                villages = json.load(f)
        except:
            villages = []
        
        # Add new village
        villages.append(village_data)
        
        # Save back
        with open('village_revenues.json', 'w') as f:
            json.dump(villages, f, indent=2)
        
        print(f"✅ Village '{village_name}' added successfully!")
        print(f"📊 Total villages in system: {len(villages)}")
        
        # Calculate new total
        total_revenue = sum(v['revenue'] for v in villages)
        print(f"💰 Total village revenue: R{total_revenue:.2f}")
        
        return {"status": "success", "total_villages": len(villages), "total_revenue": total_revenue}
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return {"status": "error", "message": str(e)}

def main():
    if len(sys.argv) < 5:
        print("Usage: python3 village_adder.py --add-village \"Village Name\" --revenue AMOUNT")
        print("Example: python3 village_adder.py --add-village \"Malamulele East\" --revenue 12500")
        return
    
    village_name = sys.argv[2]  # After --add-village
    revenue_amount = float(sys.argv[4])  # After --revenue
    
    result = add_village_to_system(village_name, revenue_amount)
    
    # Also update the main revenue data
    print("\n" + "="*50)
    print("🏛️ VILLAGE ADDITION COMPLETE")
    print("="*50)
    print(f"Village: {village_name}")
    print(f"Revenue Added: R{revenue_amount:.2f}")
    print(f"Status: {result['status']}")
    
    if result['status'] == 'success':
        print(f"\n💎 IMPERIAL EXPANSION:")
        print(f"   Total Villages: {result['total_villages']}")
        print(f"   Village Revenue: R{result['total_revenue']:.2f}")
        print(f"   Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
