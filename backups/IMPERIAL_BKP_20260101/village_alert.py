import time
import os

def check_for_new_users():
    last_count = 208 # Your current total
    print("📡 Humbu Nexus Monitoring Active...")
    print("Watching for new users in Vhulaudzi, Makhuvha, and more...")
    
    while True:
        # In a real scenario, this would check your actual database
        # For this demo, we simulate the logic
        current_count = last_count # This would be len(user_list)
        
        if current_count > last_count:
            new_user_count = current_count - last_count
            print(f"\n🔔 ALERT: {new_user_count} NEW USER(S) JOINED!")
            # Terminal beep sound
            print('\a') 
            last_count = current_count
        
        time.sleep(10) # Checks every 10 seconds

if __name__ == "__main__":
    check_for_new_users()
