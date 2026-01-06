#! /usr/bin/env python3
import sys

CURRENT_SANDTON_YIELD = 185400.00
TARGET_THRESHOLD = 250000.00

def check_threshold():
    print(f"📡 MONITORING SANDTON TECH HUB...")
    print(f"Current: R{CURRENT_SANDTON_YIELD:,.2f} | Target: R{TARGET_THRESHOLD:,.2f}")
    
    if CURRENT_SANDTON_YIELD >= TARGET_THRESHOLD:
        print("🚨 ALERT: SANDTON THRESHOLD BREACHED!")
        print("🏛️ STATUS: IMPERIAL GROWTH ACCELERATED")
    else:
        remaining = TARGET_THRESHOLD - CURRENT_SANDTON_YIELD
        print(f"📉 Status: R{remaining:,.2f} remaining until Milestone.")

if __name__ == "__main__":
    check_threshold()
