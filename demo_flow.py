"""
Demo script showing the new login-first flow
Run this to see an automated demo of the system
"""

from secure_login import SimpleLoginRateLimiter
import time

def demo():
    print("\n" + "🎬 "*30)
    print("AUTOMATED DEMO - Secure Login System v3.0")
    print("🎬 "*30)
    print("\nThis demo shows the new login-first flow with improved UI\n")
    
    time.sleep(2)
    
    # Initialize system
    print("1️⃣  Initializing system...")
    limiter = SimpleLoginRateLimiter(max_attempts=5, log_file="demo_security_log.txt")
    time.sleep(1)
    
    # Demo: Successful login
    print("\n2️⃣  Demo: Successful Login")
    print("-" * 60)
    print("Attempting login with: admin / password123")
    time.sleep(1)
    result = limiter.authenticate("admin", "password123")
    print(f"Result: {'✅ SUCCESS' if result else '❌ FAILED'}")
    time.sleep(2)
    
    # Demo: Failed attempt
    print("\n3️⃣  Demo: Failed Login Attempt")
    print("-" * 60)
    print("Attempting login with: admin / wrongpassword")
    time.sleep(1)
    result = limiter.authenticate("admin", "wrongpassword")
    print(f"Result: {'✅ SUCCESS' if result else '❌ FAILED (as expected)'}")
    time.sleep(2)
    
    # Demo: Multiple failures leading to block
    print("\n4️⃣  Demo: Account Lockout (5 Failed Attempts)")
    print("-" * 60)
    test_user = "testuser"
    for i in range(1, 6):
        print(f"\nAttempt {i}/5: {test_user} / wrongpass{i}")
        time.sleep(0.5)
        limiter.authenticate(test_user, f"wrongpass{i}")
        time.sleep(1)
    
    # Demo: Security Status
    print("\n5️⃣  Demo: Security Status Report")
    print("-" * 60)
    time.sleep(1)
    print(limiter.get_security_status())
    time.sleep(2)
    
    # Demo: Blocked users list
    print("\n6️⃣  Demo: Blocked Users List (for Unblock Menu)")
    print("-" * 60)
    blocked = limiter.get_blocked_users()
    if blocked:
        print(f"\n🚫 Currently Blocked Users ({len(blocked)}):")
        for i, user in enumerate(blocked, 1):
            attempts = limiter.failed_attempts.get(user, 0)
            print(f"  {i}. {user} - Failed attempts: {attempts}")
    time.sleep(2)
    
    # Demo: Unblock
    print("\n7️⃣  Demo: Unblocking User")
    print("-" * 60)
    if blocked:
        user_to_unblock = blocked[0]
        print(f"Unblocking: {user_to_unblock}")
        time.sleep(1)
        limiter.unblock_user(user_to_unblock)
        print(f"✅ {user_to_unblock} has been unblocked!")
    time.sleep(2)
    
    # Demo: View logs
    print("\n8️⃣  Demo: Security Log Entries")
    print("-" * 60)
    try:
        with open(limiter.log_file, 'r') as f:
            lines = f.readlines()
            print(f"\nShowing last 10 entries:")
            for line in lines[-10:]:
                print(line.rstrip())
    except:
        print("No log file yet")
    
    time.sleep(2)
    
    # Summary
    print("\n" + "="*60)
    print("DEMO COMPLETE!")
    print("="*60)
    print("\n✅ New Features Demonstrated:")
    print("   • Login-first flow (must authenticate to access features)")
    print("   • Dashboard menu appears after successful login")
    print("   • Blocked users list shown before unblocking")
    print("   • Clear security status reports")
    print("   • Comprehensive logging")
    print("\n📝 Check 'demo_security_log.txt' to see all logged events")
    print("\n🚀 Now run 'python simple_secure_login.py' to try it yourself!")
    print("="*60 + "\n")

if __name__ == "__main__":
    demo()