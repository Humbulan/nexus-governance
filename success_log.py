#! /usr/bin/env python3
import json
import os
from datetime import datetime

class SuccessLog:
    def __init__(self):
        self.log_file = os.path.expanduser("~/humbu_community_nexus/success_log.json")
        self.data = self.load_data()
        self.target_5m = 5000000  # R5M annual target
        
    def load_data(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                return json.load(f)
        return {
            "clients": [],
            "total_revenue": 0,
            "total_deposits": 0,
            "monthly_recurring": 0,
            "target_5m_progress": 0,
            "food_coverage": {
                "groceries": 2500,
                "data_airtime": 500,
                "family_support": 4000,
                "total_needed": 7000
            },
            "log_entries": []
        }
    
    def save_data(self):
        with open(self.log_file, "w") as f:
            json.dump(self.data, f, indent=2)
    
    def log_client(self, name, business, tier, monthly_fee, deposit_paid=False):
        client_id = len(self.data["clients"]) + 1
        
        client = {
            "id": client_id,
            "name": name,
            "business": business,
            "tier": tier,
            "monthly_fee": monthly_fee,
            "deposit_paid": deposit_paid,
            "deposit_amount": monthly_fee * 0.5 if deposit_paid else 0,
            "signed_date": datetime.now().isoformat(),
            "status": "active" if deposit_paid else "pending_deposit"
        }
        
        self.data["clients"].append(client)
        
        # Update financials
        if deposit_paid:
            self.data["total_deposits"] += client["deposit_amount"]
        
        self.data["monthly_recurring"] += monthly_fee
        self.data["total_revenue"] = self.data["total_deposits"] + self.data["monthly_recurring"]
        
        # Update 5M target progress (annualized)
        annual_revenue = self.data["monthly_recurring"] * 12
        self.data["target_5m_progress"] = (annual_revenue / self.target_5m) * 100
        
        # Log entry
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": "client_signed",
            "client": name,
            "business": business,
            "tier": tier,
            "monthly_fee": monthly_fee,
            "deposit_paid": deposit_paid
        }
        self.data["log_entries"].append(log_entry)
        
        self.save_data()
        
        print(f"✅ CLIENT LOGGED: {name}")
        print(f"   Business: {business}")
        print(f"   Tier: {tier} (R{monthly_fee}/month)")
        print(f"   Deposit: {'PAID R' + str(client['deposit_amount']) if deposit_paid else 'PENDING'}")
        print(f"   Status: {client['status']}")
    
    def log_payment(self, client_id, amount, payment_type="deposit"):
        for client in self.data["clients"]:
            if client["id"] == client_id:
                client["deposit_paid"] = True
                client["deposit_amount"] = amount
                client["status"] = "active"
                
                # Update financials
                if payment_type == "deposit":
                    self.data["total_deposits"] += amount
                else:
                    self.data["monthly_recurring"] += amount
                
                self.data["total_revenue"] = self.data["total_deposits"] + self.data["monthly_recurring"]
                
                # Log entry
                log_entry = {
                    "timestamp": datetime.now().isoformat(),
                    "action": "payment_received",
                    "client": client["name"],
                    "amount": amount,
                    "type": payment_type
                }
                self.data["log_entries"].append(log_entry)
                
                self.save_data()
                
                print(f"💰 PAYMENT LOGGED: R{amount} from {client['name']}")
                return True
        
        print(f"❌ Client ID {client_id} not found")
        return False
    
    def show_dashboard(self):
        print("📊 HUMBU IMPERIAL SUCCESS DASHBOARD")
        print("=" * 50)
        
        print(f"💰 FINANCIAL SUMMARY:")
        print(f"   Monthly Recurring: R{self.data['monthly_recurring']:,.2f}")
        print(f"   Total Deposits:    R{self.data['total_deposits']:,.2f}")
        print(f"   Total Revenue:     R{self.data['total_revenue']:,.2f}")
        print(f"   Active Clients:    {len([c for c in self.data['clients'] if c['status'] == 'active'])}")
        
        print(f"\n🎯 R5M TARGET PROGRESS:")
        annual_revenue = self.data['monthly_recurring'] * 12
        print(f"   Annual Revenue:    R{annual_revenue:,.2f}")
        print(f"   Target:            R{self.target_5m:,.2f}")
        print(f"   Progress:          {self.data['target_5m_progress']:.2f}%")
        
        # Visual progress bar
        progress_bar_length = 30
        filled = int((self.data['target_5m_progress'] / 100) * progress_bar_length)
        bar = "█" * filled + "░" * (progress_bar_length - filled)
        print(f"   [{bar}]")
        
        print(f"\n🍽️  FOOD ON TABLE COVERAGE:")
        needed = self.data['food_coverage']['total_needed']
        covered = min(self.data['monthly_recurring'], needed)
        coverage_pct = (covered / needed) * 100
        
        print(f"   Needed Monthly:    R{needed:,.2f}")
        print(f"   Currently Covered: R{covered:,.2f} ({coverage_pct:.1f}%)")
        
        # Check each category
        groceries = self.data['food_coverage']['groceries']
        data_airtime = self.data['food_coverage']['data_airtime']
        family = self.data['food_coverage']['family_support']
        
        print(f"\n   Category Check:")
        print(f"   • Groceries (R{groceries}): {'✅ COVERED' if self.data['monthly_recurring'] >= groceries else '❌ NEEDED'}")
        print(f"   • Data/Airtime (R{data_airtime}): {'✅ COVERED' if self.data['monthly_recurring'] >= data_airtime else '❌ NEEDED'}")
        print(f"   • Family Support (R{family}): {'✅ COVERED' if self.data['monthly_recurring'] >= family else '❌ NEEDED'}")
        
        print(f"\n📈 RECENT ACTIVITY:")
        recent_entries = self.data['log_entries'][-5:]  # Last 5 entries
        for entry in recent_entries:
            date = entry['timestamp'][:10]
            if entry['action'] == 'client_signed':
                print(f"   📅 {date}: {entry['client']} signed ({entry['tier']})")
            elif entry['action'] == 'payment_received':
                print(f"   📅 {date}: R{entry['amount']} from {entry['client']}")
        
        print("\n" + "=" * 50)

def main():
    log = SuccessLog()
    
    print("🏆 HUMBU IMPERIAL SUCCESS LOGGER")
    print("=" * 40)
    print("1. Log New Client")
    print("2. Log Payment Received")
    print("3. Show Success Dashboard")
    print("4. View All Clients")
    print()
    
    choice = input("Select option (1-4): ")
    
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
            deposit_paid = input("Deposit paid? (y/n): ").lower() == 'y'
            log.log_client(name, business, tier_name, fee, deposit_paid)
        else:
            print("❌ Invalid tier selection")
    
    elif choice == "2":
        client_id = int(input("Client ID: "))
        amount = float(input("Amount Received: "))
        payment_type = input("Payment Type (deposit/monthly): ")
        log.log_payment(client_id, amount, payment_type)
    
    elif choice == "3":
        log.show_dashboard()
    
    elif choice == "4":
        print("\n📋 ALL CLIENTS:")
        print("-" * 40)
        for client in log.data["clients"]:
            status = "🟢 ACTIVE" if client["status"] == "active" else "🟡 PENDING"
            print(f"{client['id']}. {client['name']} - {client['business']}")
            print(f"   Tier: {client['tier']} | R{client['monthly_fee']}/month")
            print(f"   Status: {status}")
            print(f"   Signed: {client['signed_date'][:10]}")
            print()

if __name__ == "__main__":
    main()
