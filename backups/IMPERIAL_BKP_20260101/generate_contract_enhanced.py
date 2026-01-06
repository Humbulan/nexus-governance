import os
from datetime import datetime

def generate_contract(client_name="", client_business="", tier="Basic", fee=1500):
    # Calculate deposit (50%)
    deposit = fee * 0.5
    monthly_fee = fee
    
    # Service details based on tier
    service_details = {
        "Basic": "• Weekly Village Status Reports (Optimal/Delayed)\n• Top 5 High-Demand Villages\n• Email Delivery + USSD Access\n• Basic Bottleneck Alerts",
        "Advanced": "• Everything in Basic, PLUS:\n• Real-time Demand Heat Maps\n• Competitor Activity Tracking\n• Predictive Stocking Recommendations\n• Monthly Strategy Session (30 min)\n• Priority USSD Code",
        "Enterprise": "• Everything in Advanced, PLUS:\n• API Access to 40-node network\n• Custom Dashboard with branding\n• Dedicated Account Manager\n• On-ground Verification Team\n• Quarterly Expansion Consulting"
    }
    
    contract = f"""
╔══════════════════════════════════════════════════════════════════╗
║                HUMBU IMPERIAL SERVICE AGREEMENT                  ║
║              OFFICIAL BUSINESS CONTRACT - HIC/2026/001           ║
╚══════════════════════════════════════════════════════════════════╝

This Agreement is made effective as of {datetime.now().strftime('%d %B %Y')}

BETWEEN:

HUMBU IMPERIAL NEXUS
(Hereinafter referred to as "the Provider")
Operating as Humbu Imperial Intelligence Network
Contact: [Your Phone Number]
Email: [Your Email]
USSD: *134*600#

AND:

{client_name.upper() if client_name else "________________________________"}
{client_business.upper() if client_business else "________________________________"}
(Hereinafter referred to as "the Client")

────────────────────────────────────────────────────────────────────
1. SERVICES TO BE PROVIDED
The Provider agrees to render the following services:

TIER SELECTED: {tier.upper()} INTELLIGENCE SERVICE
MONTHLY FEE: R{monthly_fee:,.2f} (excluding VAT)

SERVICE DETAILS:
{service_details.get(tier, service_details['Basic'])}

────────────────────────────────────────────────────────────────────
2. TERM OF AGREEMENT
This Agreement will begin on {datetime.now().strftime('%d %B %Y')} and 
will remain in effect for 30 days. After the initial term, this 
Agreement will automatically renew on a month-to-month basis until 
terminated by either party with 14 days written notice.

────────────────────────────────────────────────────────────────────
3. PAYMENT TERMS
• Activation Deposit: R{deposit:,.2f} (50% of first month, due upon signing)
• Monthly Fee: R{monthly_fee:,.2f} (due in advance on the 1st of each month)
• Payment Methods: MTN MoMo, EFT, or Cash
• Late Payment: Services may be suspended if payment is 7+ days late

────────────────────────────────────────────────────────────────────
4. CONFIDENTIALITY
Both parties agree to maintain the confidentiality of all proprietary
information shared during this Agreement. Client route data and 
Provider village intelligence are considered confidential.

────────────────────────────────────────────────────────────────────
5. LIMITATION OF LIABILITY
The Provider makes no warranties about the accuracy of intelligence
reports. The Client uses the information at their own discretion.
Maximum liability is limited to one month's service fee.

────────────────────────────────────────────────────────────────────
6. SIGNATURES
By signing below, both parties agree to the terms outlined above.

FOR THE CLIENT:

Name: _________________________
Signature: ____________________
Date: _________________________
Position: _____________________

FOR THE PROVIDER:

Name: [Your Name]
Signature: ____________________
Date: _________________________
Position: Managing Director

────────────────────────────────────────────────────────────────────
7. PAYMENT DETAILS (Activate within 24 hours of deposit)
• MTN MoMo: [Your MoMo Number] - Reference: HIC-{client_name[:3].upper() if client_name else 'CLT'}-001
• Bank: [Your Bank Name]
• Account: [Your Account Number]
• Branch: [Your Branch Code]
• Reference: HIC-{client_name[:3].upper() if client_name else 'CLT'}-001

╔══════════════════════════════════════════════════════════════════╗
║      DATA-DRIVEN DECISIONS • RURAL INTELLIGENCE • URBAN PROFIT   ║
╚══════════════════════════════════════════════════════════════════╝
"""
    
    # Generate filename
    filename = f"CONTRACT_{client_name.replace(' ', '_') if client_name else 'TEMPLATE'}_{datetime.now().strftime('%Y%m%d')}.txt"
    filepath = os.path.expanduser(f"~/humbu_community_nexus/contracts/{filename}")
    
    # Ensure contracts directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, "w") as f:
        f.write(contract)
    
    print(f"✅ CONTRACT GENERATED: {filepath}")
    print(f"   Client: {client_name or '[To be filled]'}")
    print(f"   Tier: {tier} (R{monthly_fee}/month)")
    print(f"   Deposit Due: R{deposit}")
    
    return filepath

def generate_all_templates():
    """Generate template contracts for all tiers"""
    templates_dir = os.path.expanduser("~/humbu_community_nexus/contracts/templates")
    os.makedirs(templates_dir, exist_ok=True)
    
    tiers = [
        ("Basic", 1500),
        ("Advanced", 5000), 
        ("Enterprise", 15000)
    ]
    
    for tier_name, fee in tiers:
        template_path = generate_contract("", "", tier_name, fee)
        new_name = template_path.replace("TEMPLATE", f"TEMPLATE_{tier_name.upper()}")
        os.rename(template_path, new_name)
        print(f"📄 Template saved: {new_name}")

if __name__ == "__main__":
    print("📄 CONTRACT GENERATION SYSTEM")
    print("=" * 40)
    print("1. Generate specific client contract")
    print("2. Generate all tier templates")
    print("3. View existing contracts")
    print()
    
    choice = input("Select option (1-3): ")
    
    if choice == "1":
        name = input("Client Name: ")
        business = input("Client Business: ")
        print("\nSelect Tier:")
        print("1. Basic (R1,500/month)")
        print("2. Advanced (R5,000/month)")
        print("3. Enterprise (R15,000/month)")
        
        tier_choice = input("Tier (1-3): ")
        tiers = {"1": ("Basic", 1500), "2": ("Advanced", 5000), "3": ("Enterprise", 15000)}
        
        if tier_choice in tiers:
            tier_name, fee = tiers[tier_choice]
            generate_contract(name, business, tier_name, fee)
        else:
            print("❌ Invalid tier selection")
    
    elif choice == "2":
        generate_all_templates()
        print("\n✅ All templates generated in: ~/humbu_community_nexus/contracts/templates/")
    
    elif choice == "3":
        contracts_dir = os.path.expanduser("~/humbu_community_nexus/contracts")
        if os.path.exists(contracts_dir):
            print(f"📁 Contracts in {contracts_dir}:")
            for file in os.listdir(contracts_dir):
                if file.endswith(".txt"):
                    print(f"  • {file}")
        else:
            print("No contracts generated yet.")
