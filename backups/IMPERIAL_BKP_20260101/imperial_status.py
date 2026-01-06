import json
import os

def check_status():
    print("🏛️  HUMBU IMPERIAL: DAILY STATUS CHECK")
    print("==========================================")
    
    # Load Genesis Benchmarks
    genesis_path = os.path.expanduser("~/humbu_community_nexus/reality_corrected.json")
    with open(genesis_path, "r") as f:
        genesis = json.load(f)

    # Current Stats (Simulated for this moment)
    current_efficiency = 67.5 
    current_net_monthly = 342515.60
    
    print(f"📊 PERFORMANCE VS. GENESIS:")
    print(f"   Net Monthly:  R{current_net_monthly:,.2f} / R{genesis['adjusted_net_monthly']:,.2f}")
    print(f"   Efficiency:   {current_efficiency}% (Target: 85%)")
    
    # Growth Logic
    diff = current_net_monthly - genesis['adjusted_net_monthly']
    if diff >= 0:
        print(f"🟢 VELOCITY: +R{diff:,.2f} ahead of Genesis.")
    else:
        print(f"🔴 VELOCITY: -R{abs(diff):,.2f} below Genesis.")

    print("==========================================")
    print("🎯 NEXT ACTION: Run 'optimize-network' to close the 17.5% efficiency gap.")

if __name__ == "__main__":
    check_status()
