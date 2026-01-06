#! /usr/bin/env python3
import json
import os
from datetime import datetime

print("💰 HUMBU FINANCIAL REALITY CHECK")
print("=" * 40)

# Load or create CAC data
cac_path = os.path.expanduser("~/humbu_community_nexus/gauteng_cac.txt")
if os.path.exists(cac_path):
    with open(cac_path, "r") as f:
        monthly_cac = float(f.read().strip())
else:
    monthly_cac = 21250.0  # Default

# Calculate metrics
vhembe_revenue = 28660.03
vhembe_cac = 850
vhembe_net = vhembe_revenue - vhembe_cac

gauteng_revenue = 5000000 / 12
gauteng_net = gauteng_revenue - monthly_cac
gauteng_annual_net = gauteng_net * 12

growth_multiple = gauteng_net / vhembe_net

print(f"🌍 VHEMBE (Current):")
print(f"   Revenue: R{vhembe_revenue:,.2f}/month")
print(f"   CAC: R{vhembe_cac:,.2f}/month")
print(f"   Net: R{vhembe_net:,.2f}/month")
print(f"   Margin: {(vhembe_net/vhembe_revenue*100):.1f}%")

print(f"\n🏙️  GAUTENG (2026 Target):")
print(f"   Revenue: R{gauteng_revenue:,.2f}/month")
print(f"   CAC: R{monthly_cac:,.2f}/month")
print(f"   Net: R{gauteng_net:,.2f}/month")
print(f"   Annual Net: R{gauteng_annual_net:,.2f}")
print(f"   Margin: {(gauteng_net/gauteng_revenue*100):.1f}%")

print(f"\n🚀 GROWTH REQUIRED:")
print(f"   Revenue Multiple: {gauteng_revenue/vhembe_revenue:.1f}x")
print(f"   Net Multiple: {growth_multiple:.1f}x")
print(f"   CAC Multiple: {monthly_cac/vhembe_cac:.1f}x")

print(f"\n📊 VIABILITY CHECK:")
cac_ratio = (monthly_cac / gauteng_revenue) * 100
if cac_ratio < 30:
    print(f"   ✅ CAC Ratio: {cac_ratio:.1f}% (<30% target)")
else:
    print(f"   ⚠️  CAC Ratio: {cac_ratio:.1f}% (above 30% target)")

if growth_multiple > 10:
    print(f"   ✅ Growth Potential: {growth_multiple:.1f}x")
else:
    print(f"   ⚠️  Growth Potential: {growth_multiple:.1f}x")

print("\n" + "=" * 40)
print("💡 STRATEGY: Focus on Urban ARPU (R4,500 vs R280)")
print("   Maintain CAC < 30% of revenue")
print("   Scale from 100 to 1,200 urban users")
