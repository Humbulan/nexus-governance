import random
import os
import datetime

def calculate_recruitment_costs():
    print("📈 GAUTENG URBAN ACQUISITION COSTS (CAC) 2026")
    print("==============================================")
    
    # Urban vs Rural CAC comparison (2026 SA market data)
    rural_cac = 850  # Vhembe: word-of-mouth, USSD organic
    urban_cac_base = random.uniform(15000, 35000)  # Gauteng: digital ads, lead gen
    
    # Factors increasing urban CAC:
    competition_factor = 1.8  # 80% more competition in Gauteng
    attention_cost = 2.5      # 150% higher attention cost (urban noise)
    logistics_multiplier = 3.2 # 220% higher logistics (traffic, parking, data)
    
    # Calculate final CAC
    marketing_spend = urban_cac_base * competition_factor
    logistics_overhead = 8000 * logistics_multiplier  # Base urban logistics
    data_costs = 1200 * attention_cost  # Mobile data more expensive in urban use
    
    total_cac = marketing_spend + logistics_overhead + data_costs
    net_cac = total_cac - rural_cac  # What we're ADDING to costs
    
    print(f"🌍 RURAL CAC (Vhembe):        R{rural_cac:,.2f}")
    print(f"🏙️  URBAN BASE CAC:           R{urban_cac_base:,.2f}")
    print("")
    print(f"📊 COMPETITION FACTOR:       {competition_factor:.1f}x")
    print(f"👁️  ATTENTION COST:          {attention_cost:.1f}x")
    print(f"🚗 LOGISTICS MULTIPLIER:     {logistics_multiplier:.1f}x")
    print("")
    print(f"💸 MARKETING SPEND:          R{marketing_spend:,.2f}")
    print(f"🚛 LOGISTICS OVERHEAD:       R{logistics_overhead:,.2f}")
    print(f"📱 DATA COSTS:               R{data_costs:,.2f}")
    print(f"🛑 TOTAL MONTHLY CAC:        R{total_cac:,.2f}")
    print(f"📉 NET CAC INCREASE:         R{net_cac:,.2f} (+{net_cac/rural_cac:.1f}x rural)")
    
    # Save for net profit calculations
    cac_path = os.path.expanduser("~/humbu_community_nexus/gauteng_cac.txt")
    with open(cac_path, "w") as f:
        f.write(str(total_cac))
    
    # Calculate breakeven customers
    urban_arpu = 4500  # Average Revenue Per User (Gauteng)
    rural_arpu = 280    # Average Revenue Per User (Vhembe)
    
    breakeven_customers = total_cac / urban_arpu
    print("")
    print(f"💰 URBAN ARPU:               R{urban_arpu:,.2f}")
    print(f"🌾 RURAL ARPU:               R{rural_arpu:,.2f}")
    print(f"🎯 BREAKEVEN CUSTOMERS:      {breakeven_customers:.1f} users")
    print(f"📅 BREAKEVEN DAYS:           {(breakeven_customers * 30)/120:.1f} days (at 120 users/month)")
    
    return total_cac

if __name__ == "__main__":
    calculate_recruitment_costs()
