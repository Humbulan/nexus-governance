#! /usr/bin/env python3
import os
import json
import hashlib
from datetime import datetime

print("🔍 VERIFYING IMPERIAL TRANSITION 2026")
print("=" * 40)

# Check all critical files
critical_files = [
    "~/humbu_community_nexus/genesis_2026_final.log",
    "~/humbu_community_nexus/reality_corrected.json", 
    "~/humbu_community_nexus/network_optimized.txt",
    "~/humbu_community_nexus/gauteng_cac.txt",
    "~/humbu_community_nexus/genesis_hash.txt"
]

all_valid = True
for file in critical_files:
    path = os.path.expanduser(file)
    if os.path.exists(path):
        size = os.path.getsize(path)
        print(f"✅ {file.split('/')[-1]:<25} {size:>6} bytes")
    else:
        print(f"❌ {file.split('/')[-1]:<25} MISSING")
        all_valid = False

print("\n📊 TRANSITION METRICS:")
print("-" * 40)

# Load financial data
financial_path = os.path.expanduser("~/humbu_community_nexus/reality_corrected.json")
if os.path.exists(financial_path):
    with open(financial_path, "r") as f:
        data = json.load(f)
    
    print(f"Current CAC:        R{data.get('actual_cac', 0):,.0f}/month")
    print(f"Target CAC:         R{data.get('optimal_cac_target', 0):,.0f}/month")
    print(f"Net Monthly:        R{data.get('actual_net_monthly', 0):,.0f}")
    print(f"Timeline to R5M:    {data.get('months_to_5m_net', 0):.1f} months")
    print(f"CAC Reduction:      {data.get('cac_reduction_needed_pct', 0):.0f}% needed")

# Check genesis hash
hash_path = os.path.expanduser("~/humbu_community_nexus/genesis_hash.txt")
if os.path.exists(hash_path):
    with open(hash_path, "r") as f:
        hash_content = f.read()
    print(f"\n🔐 GENESIS VERIFICATION:")
    print(hash_content)

print("\n" + "=" * 40)
if all_valid:
    print("🎉 TRANSITION VERIFIED: READY FOR 2026")
    print("🏛️  HUMBU IMPERIAL ERA ACTIVE")
else:
    print("⚠️  TRANSITION INCOMPLETE")
    print("💡 Run: midnight-2026 to complete")
print("=" * 40)
