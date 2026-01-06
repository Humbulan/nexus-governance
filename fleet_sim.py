#! /usr/bin/env python3
import json
import time
import random
from datetime import datetime

vehicles = [f"HMB-FLEET-{i:02d}" for i in range(1, 18)]
destinations = ["Thohoyandou-F", "Maniini South", "SADC Border Link", "Vhembe District Hub", "Gauteng Gateway", "Limpopo Hub", "Maniini Main Rd"]

print("🛰️ Fleet Telemetry Stream Started...")
print("📍 Hub: Maniini Main Rd, Thohoyandou")
print("🚚 Vehicles: 17 | 📍 Destinations: 7")
print("❄️ Cold-Chain: 2°C - 5°C maintained")
print("📡 Data refresh: Every 5 seconds")

try:
    while True:
        telemetry_data = []
        for v_id in vehicles:
            status = random.choice(["In Transit", "Unloading", "Returning", "Loading", "Route Optimizing"])
            telemetry_data.append({
                "vehicle_id": v_id,
                "status": status,
                "location": random.choice(destinations),
                "load_temp": round(random.uniform(2.0, 5.0), 1),
                "efficiency": "98.4%",
                "route_optimized": True,
                "fuel_efficiency": round(random.uniform(14.5, 15.5), 1),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        
        with open("fleet_telemetry.json", "w") as f:
            json.dump(telemetry_data, f, indent=2)
        
        # Also update unified dashboard
        unified = {
            "fleet_count": 17,
            "active_vehicles": len([v for v in telemetry_data if v["status"] != "Loading"]),
            "fleet_status": "Operational",
            "cold_chain_compliance": "100%",
            "route_efficiency": "98.4%",
            "last_update": datetime.now().strftime("%H:%M:%S"),
            "active_nodes": 20,
            "village_reach": 43,
            "revenue": 595238.10
        }
        
        with open("unified_dashboard.json", "w") as f:
            json.dump(unified, f, indent=2)
        
        print(f"📡 Telemetry updated: {len(telemetry_data)} vehicles | {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(5)
        
except KeyboardInterrupt:
    print("\n🛑 Telemetry simulation stopped")
