#! /usr/bin/env python3
import json
import time
import random
from datetime import datetime, timedelta

flights = [
    {
        "flight_id": "HMB-AIR-01",
        "call_sign": "HUMBU-ALPHA",
        "route": "THY (Thohoyandou) → HRE (Harare)",
        "cargo_value": 125000,
        "cargo_type": "Herbal Exports / Agricultural",
        "status": "In Flight",
        "altitude_ft": 32000,
        "ground_speed_kts": 480,
        "eta_minutes": 45,
        "fuel_efficiency": "99.2%",
        "enquiry_ref": "#4000120009",
        "sector": "SADC Air Transport"
    },
    {
        "flight_id": "HMB-AIR-02",
        "call_sign": "HUMBU-BRAVO",
        "route": "HRE (Harare) → JNB (Johannesburg)",
        "cargo_value": 98000,
        "cargo_type": "Processed Goods",
        "status": "Scheduled",
        "altitude_ft": 0,
        "ground_speed_kts": 0,
        "eta_minutes": 120,
        "fuel_efficiency": "98.7%",
        "enquiry_ref": "#4000120009",
        "sector": "SADC Air Transport"
    },
    {
        "flight_id": "HMB-GOV-01",
        "call_sign": "IDC-OBSERVER",
        "route": "PRY (Pretoria) → THY (Thohoyandou)",
        "cargo_value": 0,
        "cargo_type": "Committee Transport",
        "status": "Approaching",
        "altitude_ft": 15000,
        "ground_speed_kts": 350,
        "eta_minutes": 25,
        "fuel_efficiency": "97.5%",
        "enquiry_ref": "IDC-VERIFICATION",
        "sector": "Government Liaison"
    }
]

print("✈️ SADC AIR CORRIDOR TELEMETRY ACTIVATED")
print("========================================")
print("🛫 Active Flights: 3")
print("📍 Hub: Thohoyandou (THY)")
print("🎯 Cargo Value: R125,000 (Primary Rotation)")
print("📋 Enquiry: #4000120009 - SENTC Status")
print("📡 Telemetry refresh: Every 10 seconds")

try:
    while True:
        # Update dynamic values
        for flight in flights:
            if flight["status"] == "In Flight":
                # Simulate altitude changes
                flight["altitude_ft"] = random.randint(31000, 34000)
                flight["ground_speed_kts"] = random.randint(470, 490)
                flight["eta_minutes"] = max(5, flight["eta_minutes"] - 1)
            elif flight["status"] == "Approaching":
                flight["altitude_ft"] = random.randint(10000, 18000)
                flight["ground_speed_kts"] = random.randint(320, 380)
                flight["eta_minutes"] = max(1, flight["eta_minutes"] - 1)
            
            flight["last_update"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            flight["timestamp"] = datetime.now().strftime("%H:%M:%S")
        
        # Save telemetry data
        with open("air_telemetry.json", "w") as f:
            json.dump(flights, f, indent=2)
        
        # Update unified dashboard with aviation metrics
        unified = {
            "total_flights": len(flights),
            "active_flights": len([f for f in flights if f["status"] in ["In Flight", "Approaching"]]),
            "total_cargo_value": sum(f["cargo_value"] for f in flights),
            "primary_cargo": flights[0]["cargo_value"],
            "aviation_status": "Operational",
            "enquiry_ref": "#4000120009",
            "last_update": datetime.now().strftime("%H:%M:%S")
        }
        
        with open("aviation_dashboard.json", "w") as f:
            json.dump(unified, f, indent=2)
        
        print(f"📡 Aviation telemetry updated: {unified['active_flights']}/{unified['total_flights']} flights active | {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(10)
        
except KeyboardInterrupt:
    print("\n🛑 Aviation telemetry stopped")
