#! /usr/bin/env python3
import math

gap = 357515.68
tier1 = 1500
tier2 = 5000
tier3 = 15000

print("==================================================")
print("       HUMBU IMPERIAL: CONTRACT FORECAST")
print(f"       GAP TO MONDAY TARGET: R{gap:,.2f}")
print("==================================================")
print(f"Option A (Tier 1 focus): {math.ceil(gap/tier1)} Retailers needed")
print(f"Option B (Tier 2 focus): {math.ceil(gap/tier2)} Distributors needed")
print(f"Option C (Tier 3 focus): {math.ceil(gap/tier3)} Enterprise partners needed")
print("--------------------------------------------------")
print("🔥 RECOMMENDED MIX FOR WEEKEND:")
print("• 2 Enterprise Clients (Tier 3)")
print("• 40 Distributors (Tier 2)")
print("• 85 Retailers (Tier 1)")
print("==================================================")
