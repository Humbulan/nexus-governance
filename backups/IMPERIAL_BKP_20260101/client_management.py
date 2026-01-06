import json
import os
from datetime import datetime, timedelta

class ClientManager:
    def __init__(self):
        self.clients_file = os.path.expanduser("~/humbu_community_nexus/clients.json")
        self.clients = self.load_clients()
        
    def load_clients(self):
        if os.path.exists(self.clients_file):
            with open(self.clients_file, "r") as f:
                return json.load(f)
        return {"clients": [], "revenue": 0, "target": 15000}
    
    def save_clients(self):
        with open(self.clients_file, "w") as f:
            json.dump(self.clients, f, indent=2)
    
    def add_client(self, name, business, tier, phone, monthly_fee):
        client_id = len(self.clients["clients"]) + 1
        client = {
            "id": client_id,
            "name": name,
            "business": business,
            "tier": tier,
            "phone": phone,
            "monthly_fee": monthly_fee,
            "joined": datetime.now().isoformat(),
            "next_payment": (datetime.now() + timedelta(days=30)).isoformat(),
            "status": "active",
            "notes": ""
        }
        
        self.clients["clients"].append(client)
        self.clients["revenue"] += monthly_fee
        self.save_clients()
        
        print(f"✅ CLIENT ADDED: {name}")
        print(f"   Business: {business}")
        print(f"   Tier: {tier} (R{monthly_fee}/month)")
        print(f"   Revenue: R{self.clients['revenue']}/month total")
        print(f"   Target: R{self.clients['target']}/month")
        print(f"   Progress: {(self.clients['revenue']/self.clients['target'])*100:.1f}%")
        
        return client_id
    
    def list_clients(self):
        print("📋 ACTIVE CLIENTS")
        print("=" * 40)
        for client in self.clients["clients"]:
            if client["status"] == "active":
                print(f"{client['id']}. {client['name']} - {client['business']}")
                print(f"   Tier: {client['tier']} | R{client['monthly_fee']}/month")
                print(f"   Joined: {client['joined'][:10]}")
                print(f"   Next Payment: {client['next_payment'][:10]}")
                print()
        
        print(f"💰 MONTHLY REVENUE: R{self.clients['revenue']}")
        print(f"🎯 TARGET: R{self.clients['target']}")
        print(f"📈 PROGRESS: {(self.clients['revenue']/self.clients['target'])*100:.1f}%")
        
        # Food on table calculation
        groceries = 2500
        data_airtime = 500
        family_support = 4000
        total_needs = groceries + data_airtime + family_support
        
        print(f"\n🍽️  FOOD ON TABLE ANALYSIS:")
        print(f"   Groceries (R{groceries}): {'✅' if self.clients['revenue'] >= groceries else '❌'}")
        print(f"   Data/Airtime (R{data_airtime}): {'✅' if self.clients['revenue'] >= data_airtime else '❌'}")
        print(f"   Family Support (R{family_support}): {'✅' if self.clients['revenue'] >= family_support else '❌'}")
        print(f"   Total Needs: R{total_needs}")
        print(f"   Coverage: {(self.clients['revenue']/total_needs)*100:.1f}%")
    
    def generate_invoice(self, client_id):
        for client in self.clients["clients"]:
            if client["id"] == client_id:
                invoice = f"""
╔══════════════════════════════════════════════╗
║            HUMBU IMPERIAL INVOICE            ║
╚══════════════════════════════════════════════╝

Invoice No: HI-{datetime.now().strftime('%Y%m%d')}-{client_id:03d}
Date: {datetime.now().strftime('%d %B %Y')}

BILL TO:
{client['name']}
{client['business']}
{client['phone']}

DESCRIPTION:
{client['tier']} Intelligence Service
Monthly Access Fee

AMOUNT DUE: R{client['monthly_fee']:,.2f}

PAYMENT METHODS:
1. MTN MoMo: Send to [Your Number]
2. Cash: In-person collection
3. EFT: Bank details on request

PAYMENT DUE: {client['next_payment'][:10]}

TERMS:
• Service: {client['tier']} Intelligence Package
• Period: Monthly, auto-renewing
• Cancellation: 7 days notice required
• Support: *134*600# or WhatsApp

"Data-Driven Decisions. Rural Intelligence."
                """
                
                invoice_path = os.path.expanduser(f"~/humbu_community_nexus/invoice_{client_id}.txt")
                with open(invoice_path, "w") as f:
                    f.write(invoice)
                
                print(f"📄 INVOICE GENERATED: {invoice_path}")
                return invoice_path

def main():
    manager = ClientManager()
    
    print("🏢 HUMBU IMPERIAL CLIENT MANAGEMENT")
    print("=" * 40)
    print("1. Add New Client")
    print("2. List Active Clients")
    print("3. Generate Invoice")
    print("4. Revenue Analysis")
    print("")
    
    choice = input("Select option (1-4): ")
    
    if choice == "1":
        name = input("Client Name: ")
        business = input("Business Type: ")
        print("Tiers: 1=R1,500 | 2=R5,000 | 3=R15,000")
        tier_choice = input("Tier (1-3): ")
        tiers = {"1": ["Basic", 1500], "2": ["Advanced", 5000], "3": ["Enterprise", 15000]}
        
        if tier_choice in tiers:
            tier_name, fee = tiers[tier_choice]
            phone = input("Phone Number: ")
            manager.add_client(name, business, tier_name, phone, fee)
        else:
            print("❌ Invalid tier choice")
    
    elif choice == "2":
        manager.list_clients()
    
    elif choice == "3":
        client_id = int(input("Client ID: "))
        manager.generate_invoice(client_id)
    
    elif choice == "4":
        manager.list_clients()

if __name__ == "__main__":
    main()
