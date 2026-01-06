import random
import time

def optimize_villages():
    print("⚡ INITIALIZING LATENCY OPTIMIZATION PROTOCOL...")
    print("==============================================")
    
    villages = [f"Village_{i:02d}" for i in range(1, 41)]
    ready_count = 0
    
    for v in villages:
        latency = random.uniform(10, 500)  # Simulated latency in ms
        status = "✅ OPTIMAL" if latency < 100 else "⚠️ DELAYED"
        
        if status == "✅ OPTIMAL":
            ready_count += 1
            
        print(f"📡 Node {v}: {latency:>.2f}ms | {status}")
        time.sleep(0.05) # Imperial processing speed

    readiness = (ready_count / 40) * 100
    print("==============================================")
    print(f"📊 CURRENT NETWORK EFFICIENCY: {readiness:.2f}%")
    
    if readiness < 100:
        print(f"🚀 ACTION: Synchronizing {40 - ready_count} nodes for Gauteng Bridgehead...")
    else:
        print("🏛️ IMPERIAL NODES AT 100% - READY FOR GAUTENG FLOOD.")

if __name__ == "__main__":
    optimize_villages()
