#! /usr/bin/env python3
import os
import time
import subprocess

TARGET = 500000.00
# Current Realized Total from Surge
CURRENT = 452730.15 

def sound_alarm():
    # Trigger terminal bell and high-priority notification
    print("\a" * 5) # Terminal Beep
    subprocess.run([
        "termux-notification",
        "--title", "🏛️ MILESTONE BREACH: R500,000.00",
        "--content", f"The Imperial Grid has crossed the half-million mark: R{CURRENT:,.2f}",
        "--priority", "high",
        "--vibrate", "1000,500,1000"
    ])

if __name__ == "__main__":
    if CURRENT >= TARGET:
        sound_alarm()
        print("🚨 MILESTONE BREACHED! ALERTS DISPATCHED.")
    else:
        gap = TARGET - CURRENT
        print(f"📡 SONAR ACTIVE: R{gap:,.2f} remaining to R500k.")
