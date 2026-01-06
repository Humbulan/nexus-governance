#! /usr/bin/env python3
import json
import os

print("💰 HUMBU IMPERIAL: REALITY-ADJUSTED FINANCIAL MODEL")
print("=" * 50)

# ACTUAL DATA FROM YOUR SYSTEM
actual_cac = 74151.07  # From your transition-2026 output
actual_cac_ratio = 0.167  # 16.7% from your output

# Calculate based on reality
gauteng_monthly_revenue = 416666.67
actual_net_monthly = gauteng_monthly_revenue - actual_cac
actual_net_annual = actual_net_monthly * 12

vhembe_net = 28660.03 - 850  # R27,810
growth_multiple = actual_net_monthly / vhembe_net

print(f"📊 REALITY CHECK (Based on System Data):")
print(f"   Urban CAC: R{actual_cac:,.2f}/month")
print(f"   CAC Ratio: {actual_cac_ratio*100:.1f}% of revenue")
print(f"   Net Monthly: R{actual_net_monthly:,.2f}")
print(f"   Net Annual: R{actual_net_annual:,.2f}")
print(f"   Growth Multiple: {growth_multiple:.1f}x Vhembe")

print(f"\n⚠️  CRITICAL FINDING:")
print(f"   Your CAC is {actual_cac/21250:.1f}x higher than estimated!")
print(f"   This reduces net profit by R{actual_cac-21250:,.0f}/month")

print(f"\n🎯 ADJUSTED TARGET ACHIEVEMENT:")
print(f"   Original R5M Target: 12 months")
print(f"   Adjusted Timeline: {5000000/actual_net_annual:.1f} months")
print(f"   New Annual Target: R{actual_net_annual:,.0f}")

print(f"\n🚀 REQUIRED STRATEGY SHIFT:")
print(f"   1. Increase ARPU from R4,500 to R{4500*(actual_cac/21250):,.0f}")
print(f"   2. Reduce CAC by {(1-(21250/actual_cac))*100:.0f}%")
print(f"   3. Scale users from 1,200 to {1200*(actual_cac/21250):.0f}")

print(f"\n📈 OPTIMIZATION PRIORITIES:")
print(f"   1. Fix network latency (17.5% efficiency → target 85%+)")
print(f"   2. Urban partnership model to share CAC")
print(f"   3. Tiered pricing: R4,500 basic, R8,500 premium")
print(f"   4. CAC-to-LTV ratio: Target 1:4 (currently 1:5.6)")

# Save adjusted reality
adjusted_data = {
    "reality_checked": True,
    "actual_cac": actual_cac,
    "actual_cac_ratio": actual_cac_ratio,
    "adjusted_net_monthly": actual_net_monthly,
    "adjusted_net_annual": actual_net_annual,
    "growth_multiple": growth_multiple,
    "required_arpu_increase": actual_cac/21250,
    "new_timeline_months": 5000000/actual_net_annual,
    "critical_finding": "CAC is 3.5x higher than estimated"
}

with open(os.path.expanduser("~/humbu_community_nexus/reality_adjusted.json"), "w") as f:
    json.dump(adjusted_data, f, indent=2)

print(f"\n✅ REALITY DATA SAVED: ~/humbu_community_nexus/reality_adjusted.json")
