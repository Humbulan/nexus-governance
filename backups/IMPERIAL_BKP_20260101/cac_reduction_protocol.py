import json
import os

def apply_partnership():
    print("🤝 INITIATING URBAN PARTNERSHIP PROTOCOL")
    print("==========================================")
    
    path = os.path.expanduser("~/humbu_community_nexus/reality_adjusted.json")
    if not os.path.exists(path):
        print("❌ Error: reality_adjusted.json not found.")
        return

    with open(path, "r") as f:
        data = json.load(f)

    # Partnership Logic: 50% CAC Reduction
    old_cac = data['actual_cac']
    new_cac = old_cac * 0.50  # Strategic Split
    
    old_net = data['adjusted_net_monthly']
    new_net = 416666.67 - new_cac
    
    print(f"📉 PRE-PARTNERSHIP CAC:  R{old_cac:,.2f}")
    print(f"🛡️  POST-PARTNERSHIP CAC: R{new_cac:,.2f}")
    print(f"💰 MONTHLY NET GAIN:    +R{new_net - old_net:,.2f}")
    print("==========================================")

    # Save the Optimized Reality
    data['actual_cac'] = new_cac
    data['adjusted_net_monthly'] = new_net
    data['adjusted_net_annual'] = new_net * 12
    data['new_timeline_months'] = 5000000 / (new_net * 12)
    
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    
    print("✅ PARTNERSHIP MODEL SAVED TO reality_adjusted.json")

if __name__ == "__main__":
    apply_partnership()
