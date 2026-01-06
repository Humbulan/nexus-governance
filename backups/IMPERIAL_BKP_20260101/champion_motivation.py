import sqlite3
import csv
from datetime import datetime

def generate_motivation():
    print(f"🌟 HUMBU CEO'S CHAMPION REPORT - {datetime.now().strftime('%Y-%m-%d')}")
    print("============================================================")
    
    # 1. Get Category Value from SQL
    conn = sqlite3.connect('community_nexus.db')
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(price * stock_quantity) FROM marketplace WHERE category = 'Agriculture'")
    agri_value = cursor.fetchone()[0] or 0
    conn.close()

    # 2. Process Champions from CSV
    print(f"Total Agriculture Value in Nexus: R{agri_value:,.2f}\n")
    print(f"{'VILLAGE':<15} | {'CHAMPIONS':<15} | {'TARGET':<8} | {'REMAINING'}")
    print("-" * 60)

    try:
        with open('champion_assignments.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                village = row['Village']
                champs = f"{row['Champion 1']} & {row['Champion 2']}"
                target = row['Target Users']
                rem = row['Remaining']
                
                print(f"{village:<15} | {champs:<15} | {target:<8} | {rem}")
                # Motivation Logic
                if int(rem) > 20:
                    print(f"   💡 TIP: {row['Champion 1']}, push for 5 more sign-ups tonight!")
    except Exception as e:
        print(f"Error reading CSV: {e}")

    print("============================================================")
    print("CEO ACTION: Copy these tips to the Champions WhatsApp Group!")

if __name__ == "__main__":
    generate_motivation()
