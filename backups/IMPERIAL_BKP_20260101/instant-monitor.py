#!/usr/bin/env python3
import requests
import time

print("⚡ Instant Monitor Started")
while True:
    try:
        requests.get("http://localhost:11434/api/tags", timeout=5)
        print(f"[{time.strftime('%H:%M:%S')}] ✅ System OK")
    except:
        print(f"[{time.strftime('%H:%M:%S')}] ❌ System Down")
    time.sleep(30)
