import json
import os

def visualize_funnel():
    print("🔄 CAC FUNNEL VISUALIZATION")
    print("============================")
    
    # Check if file exists, create default if not
    net_targets_path = os.path.expanduser("~/humbu_community_nexus/net_targets.json")
    if not os.path.exists(net_targets_path):
        print("⚠️  No financial data found. Running CAC calculation first...")
        os.system("python3 ~/humbu_community_nexus/gauteng_recruitment.py")
        
        # Create default targets
        default_targets = {
            "monthly_gross": 416666.67,
            "monthly_cac": 21250.0,
            "monthly_net": 395416.67,
            "annual_net": 4745000.0,
            "calculated_at": "2025-12-31"
        }
        with open(net_targets_path, "w") as f:
            json.dump(default_targets, f, indent=2)
    
    # Load targets
    with open(net_targets_path, "r") as f:
        targets = json.load(f)
    
    revenue = targets['monthly_gross']
    cac = targets['monthly_cac']
    net = targets['monthly_net']
    
    # Visual bars
    def create_bar(value, max_val=500000, width=40):
        filled = int((value / max_val) * width)
        return "█" * filled + "░" * (width - filled)
    
    print(f"\n📊 REVENUE:    R{revenue:,.2f}")
    print(create_bar(revenue, 500000))
    
    print(f"\n💸 CAC:        R{cac:,.2f} ({cac/revenue*100:.1f}%)")
    print(create_bar(cac, 500000))
    
    print(f"\n💰 NET:        R{net:,.2f} ({net/revenue*100:.1f}%)")
    print(create_bar(net, 500000))
    
    # Funnel metrics
    print(f"\n🎯 FUNNEL EFFICIENCY:")
    print(f"   CAC-to-Revenue Ratio:  {cac/revenue*100:.1f}%")
    print(f"   Net Margin:            {net/revenue*100:.1f}%")
    print(f"   Required Conversion:   {(cac/4500):.0f} customers/month")
    print(f"   CAC Payback Period:    {cac/(net/30):.1f} days")
    
    # Health check
    print(f"\n📈 HEALTH CHECK:")
    if cac/revenue < 0.3:
        print(f"   ✅ CAC ratio is healthy (<30%)")
    else:
        print(f"   ⚠️  CAC ratio is high ({cac/revenue*100:.1f}%)")
        
    if net/revenue > 0.4:
        print(f"   ✅ Net margin is strong (>40%)")
    else:
        print(f"   ⚠️  Net margin needs improvement ({net/revenue*100:.1f}%)")

if __name__ == "__main__":
    visualize_funnel()
