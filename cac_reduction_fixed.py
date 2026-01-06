#! /usr/bin/env python3
import json
import os

print("🎯 CORRECTED CAC REDUCTION STRATEGY")
print("=" * 40)

# Load data
with open(os.path.expanduser("~/humbu_community_nexus/reality_corrected.json"), "r") as f:
    data = json.load(f)

current_cac = data['actual_cac']
target_cac = 26000  # REALISTIC 65% reduction target
reduction_pct = ((current_cac - target_cac) / current_cac) * 100

print(f"📊 REALISTIC TARGETS:")
print(f"   Current CAC:    R{current_cac:,.0f}/month")
print(f"   Target CAC:     R{target_cac:,.0f}/month")
print(f"   Reduction:      {reduction_pct:.0f}% (realistic)")
print(f"   Timeline:       6 months")

print(f"\n🚀 3-PHASE REALISTIC REDUCTION:")
print(f"\nPHASE 1: Months 1-2 (Quick Wins)")
print(f"   • Partner Sharing:   -25% (R18,538)")
print(f"   • Digital Tools:     -15% (R11,123)")
print(f"   • Route Opt:         -10% (R7,415)")
print(f"   Phase 1 CAC: R{current_cac * 0.5:,.0f}/month")

print(f"\nPHASE 2: Months 3-4 (Optimization)")
print(f"   • Bulk Purchases:    -20% (R14,830)")
print(f"   • Referral Program:  -15% (R11,123)")
print(f"   • Automation:        -10% (R7,415)")
print(f"   Phase 2 CAC: R{current_cac * 0.3:,.0f}/month")

print(f"\nPHASE 3: Months 5-6 (Scale)")
print(f"   • Brand Recognition: -15% (R11,123)")
print(f"   • Repeat Business:   -10% (R7,415)")
print(f"   • Network Effects:   -5% (R3,708)")
print(f"   Phase 3 CAC: R{target_cac:,.0f}/month")

print(f"\n📈 IMPACT ON TIMELINE:")
new_net = 416667 - target_cac  # R390,667/month
new_timeline = 5000000 / new_net  # 12.8 months
print(f"   With R{target_cac:,.0f} CAC:")
print(f"   • Net Monthly: R{new_net:,.0f}")
print(f"   • Timeline: {new_timeline:.1f} months")
print(f"   • Improvement: -{14.6 - new_timeline:.1f} months")

# Save corrected plan
corrected_plan = {
    "realistic_target_cac": target_cac,
    "reduction_percentage": reduction_pct,
    "phase1_cac": current_cac * 0.5,
    "phase2_cac": current_cac * 0.3,
    "phase3_cac": target_cac,
    "new_net_monthly": new_net,
    "new_timeline_months": new_timeline,
    "improvement_months": 14.6 - new_timeline
}

with open(os.path.expanduser("~/humbu_community_nexus/cac_corrected_plan.json"), "w") as f:
    json.dump(corrected_plan, f, indent=2)

print(f"\n✅ CORRECTED PLAN SAVED")
