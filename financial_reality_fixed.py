#! /usr/bin/env python3
import json
import os

print("💰 HUMBU IMPERIAL: CORRECTED FINANCIAL MODEL")
print("=" * 50)

# CORRECTED CALCULATION
actual_cac = 74151.07
gauteng_monthly_revenue = 416666.67
actual_net_monthly = gauteng_monthly_revenue - actual_cac
actual_net_annual = actual_net_monthly * 12

# FIX: Timeline to reach R5M NET (not gross)
target_net = 5000000  # We want R5M NET profit, not gross revenue
months_to_target = target_net / actual_net_monthly  # CORRECTED

vhembe_net = 28660.03 - 850
growth_multiple = actual_net_monthly / vhembe_net

print(f"📊 CORRECTED REALITY:")
print(f"   Urban CAC: R{actual_cac:,.2f}/month")
print(f"   CAC Ratio: {(actual_cac/gauteng_monthly_revenue*100):.1f}%")
print(f"   Net Monthly: R{actual_net_monthly:,.2f}")
print(f"   Net Annual: R{actual_net_annual:,.2f}")
print(f"   Growth Multiple: {growth_multiple:.1f}x Vhembe")

print(f"\n🎯 CORRECTED TIMELINE TO R5M NET PROFIT:")
print(f"   Target: R5,000,000 NET (not gross)")
print(f"   Current Net/Month: R{actual_net_monthly:,.2f}")
print(f"   Months Required: {months_to_target:.1f} months")
print(f"   Years Required: {months_to_target/12:.1f} years")

print(f"\n🚀 REQUIRED STRATEGY (CORRECTED):")
# Calculate needed CAC reduction to hit 12 months
target_monthly_net = target_net / 12
required_cac = gauteng_monthly_revenue - target_monthly_net
cac_reduction_pct = (1 - (required_cac / actual_cac)) * 100

print(f"   1. Reduce CAC by {cac_reduction_pct:.0f}% (to R{required_cac:,.0f})")
print(f"   2. OR Increase revenue to R{gauteng_monthly_revenue * (months_to_target/12):,.0f}/month")
print(f"   3. OR Combination: CAC ↓ + Revenue ↑")

print(f"\n📈 OPTIMAL PATH TO 12-MONTH TIMELINE:")
optimal_monthly = target_net / 12  # R416,667/month net
optimal_cac = gauteng_monthly_revenue * 0.3  # 30% CAC ratio target
optimal_revenue_needed = optimal_monthly / (1 - 0.3)  # 70% net margin

print(f"   Target Net/Month: R{optimal_monthly:,.2f}")
print(f"   Target CAC: R{optimal_cac:,.2f} (30% of revenue)")
print(f"   Required Revenue: R{optimal_revenue_needed:,.2f}/month")
print(f"   Required ARPU: R{optimal_revenue_needed/100:.0f} (at 100 users)")

# Save corrected data
corrected_data = {
    "corrected": True,
    "actual_cac": actual_cac,
    "actual_net_monthly": actual_net_monthly,
    "actual_net_annual": actual_net_annual,
    "months_to_5m_net": months_to_target,
    "required_cac_for_12mo": required_cac,
    "cac_reduction_needed_pct": cac_reduction_pct,
    "optimal_monthly_net": optimal_monthly,
    "optimal_cac_target": optimal_cac,
    "optimal_revenue_needed": optimal_revenue_needed,
    "critical_insight": "R5M target is NET profit, timeline depends on CAC reduction"
}

with open(os.path.expanduser("~/humbu_community_nexus/reality_corrected.json"), "w") as f:
    json.dump(corrected_data, f, indent=2)

print(f"\n✅ CORRECTED DATA SAVED: ~/humbu_community_nexus/reality_corrected.json")
