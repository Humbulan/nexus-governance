import json
import os
from datetime import datetime

def generate_templates():
    templates = {}
    
    # Template 1: Short & Direct (For distributors)
    templates['distributor'] = f"""Good day [Name],

I help businesses reduce logistics waste between Gauteng and Vhembe.

Our system monitors 40 villages in real-time and shows which ones are "optimal" for deliveries vs "delayed" due to infrastructure issues.

Last month, our clients saved an average of R18,500 by avoiding wasted trips to villages with roadblocks or low demand.

Would you be open to a 10-minute call to see if this could work for your business?

*Sample village status right now:*
✅ Optimal: 27 villages ready for deliveries
⚠️ Delayed: 13 villages to avoid this week

Reply "INFO" and I'll share a free report for your top 3 villages.

- [Your Name]
Humbu Imperial Intelligence
*134*600# (Live system)
"""
    
    # Template 2: For Retailers/Shop Owners
    templates['retailer'] = f"""Hello [Name],

Do you struggle with knowing which villages have buying power each week?

We track real-time spending patterns across 40 Vhembe villages. Our system shows exactly where demand is high RIGHT NOW - not last month's data.

Example: This week, Folovhodwe shows R257 average spending per user (up 42% from last week), while Makhurha shows R62 (down 18%).

For R1,500/month (less than one wasted delivery), you get weekly intelligence on:
• Top 5 buying villages
• Price sensitivity per area
• Competitor stock levels
• Optimal delivery windows

Interested in a free sample for your business?

Reply "SAMPLE" and I'll generate one for you.

- [Your Name]
Humbu Imperial
"""
    
    # Template 3: For Agricultural Suppliers
    templates['agriculture'] = f"""Hi [Name],

Farmers in Vhembe lose 30% of their produce due to poor logistics timing.

Our system monitors:
• Which villages need maize vs vegetables THIS WEEK
• Road conditions for truck access
• Local storage capacity availability
• Real-time price differentials

Last week, we alerted clients that Malamulele had 20kg maize surplus (cheap) while Thohoyandou had shortage (premium price).

Our clients made R8,200 arbitrage profit from that one alert.

For R5,000/month, we provide:
• Daily crop availability alerts
• Optimal route planning
• Buyer/seller matching
• Price intelligence

Want to see this week's crop availability map?

Reply "CROP" for free access.

- [Your Name]
Humbu Imperial
"""
    
    # Save all templates
    for template_name, content in templates.items():
        file_path = os.path.expanduser(f"~/humbu_community_nexus/whatsapp_{template_name}.txt")
        with open(file_path, "w") as f:
            f.write(content)
        print(f"✅ Generated: {file_path}")
    
    # Create master file
    master_path = os.path.expanduser("~/humbu_community_nexus/WHATSAPP_TEMPLATES_MASTER.txt")
    with open(master_path, "w") as f:
        f.write("HUMBU IMPERIAL: WHATSAPP OUTREACH TEMPLATES\n")
        f.write("=" * 50 + "\n\n")
        for name, content in templates.items():
            f.write(f"TEMPLATE: {name.upper()}\n")
            f.write("-" * 30 + "\n")
            f.write(content)
            f.write("\n" + "=" * 50 + "\n\n")
    
    print(f"📱 MASTER TEMPLATES: {master_path}")
    
    return master_path

if __name__ == "__main__":
    generate_templates()
