import json

current_stats = {
    "thohoyandou": 71, "sibasa": 30, "malamulele": 29, 
    "lwamondo": 17, "manini": 11, "mukula": 10, 
    "mukhomi": 8, "mbilwi": 6, "tshilapfa": 5, 
    "shitale": 5, "gundo": 5, "tshitavha": 4, 
    "folovhodwe": 4, "makhuvha": 2, "vhulaudzi": 1
}

TARGET_TOTAL = 308
current_total = sum(current_stats.values())
remaining = TARGET_TOTAL - current_total

print(f"\n📈 HUMBU COMMUNITY NEXUS: GROWTH TRACKER")
print(f"==========================================")
print(f"Current Users: {current_total}")
print(f"Target Users:  {TARGET_TOTAL}")
print(f"Distance:      {remaining} users to go!")
print(f"==========================================\n")

print(f"{'VILLAGE':<15} | {'CURRENT':<8} | {'ACTION NEEDED'}")
print("-" * 45)

for village, count in current_stats.items():
    if count < 10:
        action = "🔴 CRITICAL: Needs local champion"
    elif count < 25:
        action = "🟡 GROWING: Needs more USSD training"
    else:
        action = "🟢 STRONG: Ready for MoMo rollout"
    print(f"{village.capitalize():<15} | {count:<8} | {action}")

print(f"\n🎯 FOCUS: To reach 308, we need ~7 new users per village.")
