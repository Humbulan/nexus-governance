import requests
import threading
import time
import sys
from datetime import datetime

class LoadTester:
    def __init__(self, base_url="http://localhost:8080", duration=7200):  # 2 hours
        self.base_url = base_url
        self.duration = duration
        self.results = {
            'success': 0,
            'failure': 0,
            'total_time': 0,
            'requests': 0
        }
        self.running = True
        self.endpoints = [
            '/',
            '/health',
            '/metrics',
            '/api/villages',
            '/api/transactions'
        ]
    
    def make_request(self, endpoint):
        start = time.time()
        try:
            response = requests.get(f"{self.base_url}{endpoint}", timeout=5)
            elapsed = time.time() - start
            
            if response.status_code == 200:
                self.results['success'] += 1
                return True, elapsed
            else:
                self.results['failure'] += 1
                return False, elapsed
        except Exception as e:
            self.results['failure'] += 1
            return False, time.time() - start
    
    def worker(self, worker_id):
        while self.running:
            for endpoint in self.endpoints:
                if not self.running:
                    break
                
                success, elapsed = self.make_request(endpoint)
                self.results['requests'] += 1
                self.results['total_time'] += elapsed
                
                # Log every 10th request
                if self.results['requests'] % 10 == 0:
                    avg_time = self.results['total_time'] / self.results['requests']
                    success_rate = (self.results['success'] / self.results['requests']) * 100
                    print(f"[Worker {worker_id}] Req {self.results['requests']}: "
                          f"{'✅' if success else '❌'} {endpoint} - "
                          f"{elapsed:.2f}s | Avg: {avg_time:.2f}s | Success: {success_rate:.1f}%")
                
                time.sleep(0.5)  # Small delay between requests
    
    def run_test(self, num_workers=3):
        print(f"🚀 STARTING LOAD TEST - {self.duration} seconds ({self.duration/3600:.1f} hours)")
        print(f"📊 Target: Maximum uptime for 2 hours")
        print(f"👥 Workers: {num_workers}")
        print(f"🌐 Base URL: {self.base_url}")
        print("=" * 60)
        
        # Start workers
        threads = []
        for i in range(num_workers):
            t = threading.Thread(target=self.worker, args=(i+1,))
            t.daemon = True
            t.start()
            threads.append(t)
        
        # Run for specified duration
        start_time = time.time()
        try:
            while time.time() - start_time < self.duration:
                elapsed = time.time() - start_time
                remaining = self.duration - elapsed
                
                # Print status every 30 seconds
                if int(elapsed) % 30 == 0:
                    if self.results['requests'] > 0:
                        avg_time = self.results['total_time'] / self.results['requests']
                        success_rate = (self.results['success'] / self.results['requests']) * 100
                        print(f"\n📈 STATUS @ {datetime.now().strftime('%H:%M:%S')}")
                        print(f"   Time elapsed: {int(elapsed/60)}m {int(elapsed%60)}s")
                        print(f"   Time remaining: {int(remaining/60)}m {int(remaining%60)}s")
                        print(f"   Total requests: {self.results['requests']}")
                        print(f"   Success rate: {success_rate:.1f}%")
                        print(f"   Average response: {avg_time:.2f}s")
                        print(f"   Success/Failure: {self.results['success']}/{self.results['failure']}")
                        print("-" * 40)
                
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("\n⏹️  Test interrupted by user")
        
        finally:
            self.running = False
            time.sleep(2)  # Let threads finish
            
            # Final report
            print("\n" + "=" * 60)
            print("🎯 LOAD TEST COMPLETE - FINAL REPORT")
            print("=" * 60)
            
            total_time = time.time() - start_time
            if self.results['requests'] > 0:
                avg_time = self.results['total_time'] / self.results['requests']
                success_rate = (self.results['success'] / self.results['requests']) * 100
                requests_per_second = self.results['requests'] / total_time
            else:
                avg_time = 0
                success_rate = 0
                requests_per_second = 0
            
            print(f"⏱️  Total test time: {total_time:.1f}s ({total_time/60:.1f}m)")
            print(f"📊 Total requests: {self.results['requests']}")
            print(f"✅ Successful: {self.results['success']}")
            print(f"❌ Failed: {self.results['failure']}")
            print(f"🎯 Success rate: {success_rate:.1f}%")
            print(f"⚡ Average response: {avg_time:.2f}s")
            print(f"🚀 Requests/second: {requests_per_second:.2f}")
            print(f"🏆 Uptime score: {success_rate * (self.results['requests'] / 1000):.1f}")
            
            # Save results
            with open("~/humbu_community_nexus/load_test_results.txt", "w") as f:
                f.write(f"Load Test Results - {datetime.now()}\n")
                f.write(f"Duration: {total_time:.1f}s\n")
                f.write(f"Requests: {self.results['requests']}\n")
                f.write(f"Success: {self.results['success']}\n")
                f.write(f"Failure: {self.results['failure']}\n")
                f.write(f"Success Rate: {success_rate:.1f}%\n")
                f.write(f"Avg Response: {avg_time:.2f}s\n")
                f.write(f"Requests/sec: {requests_per_second:.2f}\n")
            
            print(f"\n📄 Results saved to: ~/humbu_community_nexus/load_test_results.txt")

if __name__ == "__main__":
    # Get test duration from command line or use 2 hours
    duration = 7200  # 2 hours in seconds
    if len(sys.argv) > 1:
        try:
            duration = int(sys.argv[1])
        except:
            pass
    
    tester = LoadTester(duration=duration)
    tester.run_test(num_workers=3)
