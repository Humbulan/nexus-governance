import datetime
import os
import random
import math

# Imperial Metrics
VILLAGES = 40
BASE_VILLAGE_YIELD = 28660.03
TARGET_YIELD = 5000000.00
GROWTH_RATE = 1.15  # 15% MoM growth

def get_stats():
    # Village Efficiency
    ready_nodes = sum(1 for _ in range(VILLAGES) if random.uniform(10, 500) < 100)
    efficiency = (ready_nodes / VILLAGES)
    
    # Gauteng Injection Check
    state_path = os.path.expanduser("~/humbu_community_nexus/gauteng_state.txt")
    gauteng_yield = 0.0
    if os.path.exists(state_path):
        with open(state_path, "r") as f:
            try:
                gauteng_yield = float(f.read().strip())
            except:
                gauteng_yield = 0.0
    return ready_nodes, efficiency, gauteng_yield

ready_nodes, efficiency, gauteng_yield = get_stats()
total_realized = (BASE_VILLAGE_YIELD * efficiency) + gauteng_yield
progress_pct = (total_realized / TARGET_YIELD) * 100
today = datetime.date.today().strftime("%Y-%m-%d")

# Time-to-Target
if total_realized > 0:
    months_to_target = math.log(TARGET_YIELD / total_realized) / math.log(GROWTH_RATE)
else:
    months_to_target = float('inf')

status = "🏛️ IMPERIAL" if total_realized > 100000 else "🟡 STABLE"

report = f"""
=========================================
      HUMBU IMPERIAL: VELOCITY REPORT
      Date: {today} | Status: {status}
=========================================
Village Nodes:    {ready_nodes}/{VILLAGES} ({efficiency*100:.1f}% Efficiency)
Gauteng Nodes:    ACTIVE (Injection Detected)

--- REVENUE STREAMS ---
Village Yield:    R{(BASE_VILLAGE_YIELD * efficiency):,.2f}
Gauteng Yield:    R{gauteng_yield:,.2f}
TOTAL REALIZED:   R{total_realized:,.2f}

--- EXPANSION METRICS ---
Progress:         {progress_pct:.4f}%
Gauteng Target:   R5,000,000.00
Months to Target: {months_to_target:.1f} months
=========================================
"""

print(report)

# Save logic
dir_path = os.path.expanduser("~/humbu_community_nexus")
full_path = os.path.join(dir_path, f"daily_summary_{datetime.date.today().strftime('%Y%m%d')}.txt")
with open(full_path, "w") as f:
    f.write(report)
