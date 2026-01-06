#! /usr/bin/env python3
#!/data/data/com.termux/files/usr/bin/python3
import sys
import subprocess

def humbu_ussd_logic(msisdn, text):
    if text == "":
        return "CON 📱 HUMBU COMMUNITY NEXUS\nReg: 2024/626727/07\n1. Balance\n2. Pay (MoMo)\n3. Market\n4. Tasks\n5. Register"

    if text == "2":
        return "CON Enter Amount to Pay (ZAR):"
    
    # User entered amount, now ask for confirmation
    if text.startswith("2*") and len(text.split("*")) == 2:
        amount = text.split("*")[1]
        return f"CON Confirm R{amount} payment?\n1. Yes, Pay Now\n2. Cancel"

    # User clicked "1" to Confirm! This triggers the REAL API.
    if text.startswith("2*") and text.endswith("*1"):
        amount = text.split("*")[1]
        
        # TRIGGER THE MOMO SCRIPT WE BUILT TODAY
        # We pass the phone and amount to your final integration script
        try:
            # This calls your confirmed MoMo script in the background
            subprocess.Popen(["bash", "humbu_momo_integration_final.sh", msisdn, amount])
            return f"END Request Sent!\nCheck your phone for the PIN prompt to pay R{amount}.\nThank you, {msisdn}."
        except:
            return "END System Busy. Please try again in 5 minutes."

    return "END Thank you for using Humbu Nexus."

if __name__ == "__main__":
    phone = sys.argv[1] if len(sys.argv) > 1 else "27000000000"
    user_input = sys.argv[2] if len(sys.argv) > 2 else ""
    print(humbu_ussd_logic(phone, user_input))

def show_momo_menu():
    """Show MTN MoMo menu"""
    print("\n" + "="*50)
    print("💰 MTN MOMO INTEGRATION")
    print("="*50)
    print("1. Send Money via MTN MoMo")
    print("2. Check MoMo Balance")
    print("3. Buy Airtime")
    print("4. Transaction History")
    print("5. Back to Main Menu")
    print("="*50)

# Import MTN MoMo integration
try:
    from mobile_money.mtn_momo_real import RealMTNMomo
    MTN_MOMO_AVAILABLE = True
except:
    MTN_MOMO_AVAILABLE = False
    print("⚠️ MTN MoMo integration requires configuration")

if MTN_MOMO_AVAILABLE:
    print("\n✅ MTN MOMO INTEGRATION ACTIVE")
    print("   Real mobile money transactions enabled")
    print("   Dial *134*600# and choose 'Send Money'")
    print("   Select 'MTN MoMo' for instant transfers")

def show_momo_menu():
    """Show MTN MoMo menu"""
    print("\n" + "="*50)
    print("💰 MTN MOMO INTEGRATION")
    print("="*50)
    print("1. Send Money via MTN MoMo")
    print("2. Check MoMo Balance")
    print("3. Buy Airtime")
    print("4. Transaction History")
    print("5. Back to Main Menu")
    print("="*50)

# Import MTN MoMo integration
try:
    from mobile_money.mtn_momo_real import RealMTNMomo
    MTN_MOMO_AVAILABLE = True
except:
    MTN_MOMO_AVAILABLE = False
    print("⚠️ MTN MoMo integration requires configuration")

if MTN_MOMO_AVAILABLE:
    print("\n✅ MTN MOMO INTEGRATION ACTIVE")
    print("   Real mobile money transactions enabled")
    print("   Dial *134*600# and choose 'Send Money'")
    print("   Select 'MTN MoMo' for instant transfers")

def show_momo_menu():
    """Show MTN MoMo menu"""
    print("\n" + "="*50)
    print("💰 MTN MOMO INTEGRATION")
    print("="*50)
    print("1. Send Money via MTN MoMo")
    print("2. Check MoMo Balance")
    print("3. Buy Airtime")
    print("4. Transaction History")
    print("5. Back to Main Menu")
    print("="*50)

# Import MTN MoMo integration
try:
    from mobile_money.mtn_momo_real import RealMTNMomo
    MTN_MOMO_AVAILABLE = True
except:
    MTN_MOMO_AVAILABLE = False
    print("⚠️ MTN MoMo integration requires configuration")

if MTN_MOMO_AVAILABLE:
    print("\n✅ MTN MOMO INTEGRATION ACTIVE")
    print("   Real mobile money transactions enabled")
    print("   Dial *134*600# and choose 'Send Money'")
    print("   Select 'MTN MoMo' for instant transfers")

def show_momo_menu():
    """Show MTN MoMo menu"""
    print("\n" + "="*50)
    print("💰 MTN MOMO INTEGRATION")
    print("="*50)
    print("1. Send Money via MTN MoMo")
    print("2. Check MoMo Balance")
    print("3. Buy Airtime")
    print("4. Transaction History")
    print("5. Back to Main Menu")
    print("="*50)

# Import MTN MoMo integration
try:
    from mobile_money.mtn_momo_real import RealMTNMomo
    MTN_MOMO_AVAILABLE = True
except:
    MTN_MOMO_AVAILABLE = False
    print("⚠️ MTN MoMo integration requires configuration")

if MTN_MOMO_AVAILABLE:
    print("\n✅ MTN MOMO INTEGRATION ACTIVE")
    print("   Real mobile money transactions enabled")
    print("   Dial *134*600# and choose 'Send Money'")
    print("   Select 'MTN MoMo' for instant transfers")

def show_momo_menu():
    """Show MTN MoMo menu"""
    print("\n" + "="*50)
    print("💰 MTN MOMO INTEGRATION")
    print("="*50)
    print("1. Send Money via MTN MoMo")
    print("2. Check MoMo Balance")
    print("3. Buy Airtime")
    print("4. Transaction History")
    print("5. Back to Main Menu")
    print("="*50)

# Import MTN MoMo integration
try:
    from mobile_money.mtn_momo_real import RealMTNMomo
    MTN_MOMO_AVAILABLE = True
except:
    MTN_MOMO_AVAILABLE = False
    print("⚠️ MTN MoMo integration requires configuration")

if MTN_MOMO_AVAILABLE:
    print("\n✅ MTN MOMO INTEGRATION ACTIVE")
    print("   Real mobile money transactions enabled")
    print("   Dial *134*600# and choose 'Send Money'")
    print("   Select 'MTN MoMo' for instant transfers")

def show_momo_menu():
    """Show MTN MoMo menu"""
    print("\n" + "="*50)
    print("💰 MTN MOMO INTEGRATION")
    print("="*50)
    print("1. Send Money via MTN MoMo")
    print("2. Check MoMo Balance")
    print("3. Buy Airtime")
    print("4. Transaction History")
    print("5. Back to Main Menu")
    print("="*50)

# Import MTN MoMo integration
try:
    from mobile_money.mtn_momo_real import RealMTNMomo
    MTN_MOMO_AVAILABLE = True
except:
    MTN_MOMO_AVAILABLE = False
    print("⚠️ MTN MoMo integration requires configuration")

if MTN_MOMO_AVAILABLE:
    print("\n✅ MTN MOMO INTEGRATION ACTIVE")
    print("   Real mobile money transactions enabled")
    print("   Dial *134*600# and choose 'Send Money'")
    print("   Select 'MTN MoMo' for instant transfers")

def show_momo_menu():
    """Show MTN MoMo menu"""
    print("\n" + "="*50)
    print("💰 MTN MOMO INTEGRATION")
    print("="*50)
    print("1. Send Money via MTN MoMo")
    print("2. Check MoMo Balance")
    print("3. Buy Airtime")
    print("4. Transaction History")
    print("5. Back to Main Menu")
    print("="*50)

# Import MTN MoMo integration
try:
    from mobile_money.mtn_momo_real import RealMTNMomo
    MTN_MOMO_AVAILABLE = True
except:
    MTN_MOMO_AVAILABLE = False
    print("⚠️ MTN MoMo integration requires configuration")

if MTN_MOMO_AVAILABLE:
    print("\n✅ MTN MOMO INTEGRATION ACTIVE")
    print("   Real mobile money transactions enabled")
    print("   Dial *134*600# and choose 'Send Money'")
    print("   Select 'MTN MoMo' for instant transfers")
