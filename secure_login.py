import datetime
from collections import defaultdict
import os

class SimpleLoginRateLimiter:
    """Simple login system with plain text passwords for easy testing."""
    
    def __init__(self, max_attempts=5, log_file="security_log.txt"):
        self.max_attempts = max_attempts
        self.log_file = log_file
        self.failed_attempts = defaultdict(int)
        self.blocked_users = set()
        
        # Valid credentials (plain text for simplicity)
        self.valid_credentials = {
            "admin": "password123",
            "user": "userpass",
            "test": "test123"
        }
    
    def log_event(self, message):
        """Log security events to a file with timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        try:
            with open(self.log_file, "a") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"[ERROR] Failed to write to log: {e}")
    
    def is_blocked(self, username):
        """Check if a user is blocked."""
        return username in self.blocked_users
    
    def block_user(self, username):
        """Block a user and log the event."""
        self.blocked_users.add(username)
        message = f"SECURITY ALERT - User '{username}' blocked after {self.max_attempts} failed attempts"
        self.log_event(message)
        print(f"\n🚫 User '{username}' is temporarily blocked due to too many failed attempts.")
    
    def unblock_user(self, username):
        """Unblock a user."""
        if username in self.blocked_users:
            self.blocked_users.remove(username)
            if username in self.failed_attempts:
                del self.failed_attempts[username]
            self.log_event(f"User '{username}' was unblocked")
            return True
        return False
    
    def record_failed_attempt(self, username):
        """Record a failed login attempt."""
        self.failed_attempts[username] += 1
        attempts = self.failed_attempts[username]
        
        self.log_event(f"Failed login attempt for '{username}' (Attempt {attempts}/{self.max_attempts})")
        
        if attempts >= self.max_attempts:
            self.block_user(username)
        else:
            remaining = self.max_attempts - attempts
            print(f"⚠️  Warning: {remaining} attempt(s) remaining before lockout.")
    
    def authenticate(self, username, password):
        """Authenticate user credentials."""
        if self.is_blocked(username):
            print(f"\n🚫 User '{username}' is temporarily blocked due to too many failed attempts.")
            self.log_event(f"Blocked user '{username}' attempted login")
            return False
        
        if username in self.valid_credentials and self.valid_credentials[username] == password:
            # Reset failed attempts on successful login
            if username in self.failed_attempts:
                del self.failed_attempts[username]
            
            self.log_event(f"Successful login for user '{username}'")
            return True
        else:
            print(f"\n❌ Invalid username or password.")
            self.record_failed_attempt(username)
            return False
    
    def get_security_status(self):
        """Get formatted security status."""
        lines = []
        lines.append("\n" + "="*70)
        lines.append("SECURITY STATUS REPORT")
        lines.append("="*70)
        lines.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"Max Failed Attempts: {self.max_attempts}")
        lines.append("")
        
        if self.blocked_users:
            lines.append(f"🚫 Blocked Users ({len(self.blocked_users)}):")
            for user in sorted(self.blocked_users):
                attempts = self.failed_attempts.get(user, 0)
                lines.append(f"   - {user} (Failed attempts: {attempts})")
        else:
            lines.append("✅ No blocked users")
        
        lines.append("")
        
        active_attempts = {u: c for u, c in self.failed_attempts.items() if u not in self.blocked_users}
        if active_attempts:
            lines.append(f"⚠️  Users with Failed Attempts:")
            for user, count in sorted(active_attempts.items()):
                status = "⚠️ " if count >= 3 else "  "
                lines.append(f"   {status}{user}: {count}/{self.max_attempts} attempts")
        else:
            lines.append("✅ No recent failed attempts")
        
        lines.append("="*70 + "\n")
        return "\n".join(lines)
    
    def get_blocked_users(self):
        """Get sorted list of blocked users."""
        return sorted(list(self.blocked_users))


def clear_screen():
    """Clear console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def login_screen(rate_limiter):
    """Handle login screen."""
    while True:
        clear_screen()
        print("\n" + "="*70)
        print("           🔐 SECURE LOGIN SYSTEM")
        print("="*70)
        print("  Protected with Rate Limiting & Security Logging")
        print("="*70)
        print("\n📝 Please enter your credentials")
        print("-"*70)
        print("Available test accounts:")
        print("  • admin / password123")
        print("  • user / userpass")
        print("  • test / test123")
        print("-"*70)
        
        username = input("\nUsername: ").strip()
        if not username:
            print("\n❌ Username cannot be empty.")
            input("\nPress Enter to try again...")
            continue
        
        password = input("Password: ").strip()
        if not password:
            print("\n❌ Password cannot be empty.")
            input("\nPress Enter to try again...")
            continue
        
        print("\n🔄 Authenticating...")
        if rate_limiter.authenticate(username, password):
            print(f"\n✅ Login successful! Welcome, {username}!")
            input("\nPress Enter to continue to dashboard...")
            return username
        else:
            input("\nPress Enter to try again...")


def view_security_logs(rate_limiter):
    """Display security logs."""
    clear_screen()
    print("\n" + "="*70)
    print("SECURITY LOGS - RECENT ENTRIES (Last 30)")
    print("="*70)
    
    try:
        with open(rate_limiter.log_file, 'r') as f:
            lines = f.readlines()
            
            if not lines:
                print("\n📄 No log entries found.")
            else:
                recent = lines[-30:]
                for line in recent:
                    print(line.rstrip())
                print(f"\n📊 Showing {len(recent)} of {len(lines)} total entries")
    except FileNotFoundError:
        print("\n❌ No log file found yet.")
    
    print("="*70)


def unblock_user_menu(rate_limiter):
    """Handle user unblocking."""
    clear_screen()
    print("\n" + "="*70)
    print("UNBLOCK USER - ADMINISTRATION")
    print("="*70)
    
    blocked = rate_limiter.get_blocked_users()
    
    if not blocked:
        print("\n✅ No users are currently blocked.")
    else:
        print(f"\n🚫 Currently Blocked Users ({len(blocked)}):")
        print("-"*70)
        for i, user in enumerate(blocked, 1):
            attempts = rate_limiter.failed_attempts.get(user, 0)
            print(f"  {i}. {user} - Failed attempts: {attempts}")
        print("-"*70)
        
        username = input("\nEnter username to unblock (or press Enter to cancel): ").strip()
        
        if not username:
            print("\n↩️  Cancelled.")
        elif username in blocked:
            rate_limiter.unblock_user(username)
            print(f"\n✅ User '{username}' has been unblocked successfully!")
            print("   Failed attempt counter reset.")
        else:
            print(f"\n❌ User '{username}' is not in the blocked list.")
    
    print("="*70)


def dashboard(rate_limiter, username):
    """Main dashboard after login."""
    while True:
        clear_screen()
        print("\n" + "="*70)
        print("           🔐 DASHBOARD")
        print("="*70)
        print(f"  Logged in as: {username}")
        print(f"  Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)
        
        print("\n📋 MAIN MENU")
        print("-"*70)
        print("1. 📊 View Security Status")
        print("2. 📄 View Security Logs")
        print("3. 🔓 Unblock User")
        print("4. ℹ️  System Info")
        print("5. 🚪 Logout")
        print("-"*70)
        
        choice = input("\nSelect (1-5): ").strip()
        
        if choice == "1":
            clear_screen()
            print(rate_limiter.get_security_status())
            input("\nPress Enter to continue...")
        
        elif choice == "2":
            view_security_logs(rate_limiter)
            input("\nPress Enter to continue...")
        
        elif choice == "3":
            unblock_user_menu(rate_limiter)
            input("\nPress Enter to continue...")
        
        elif choice == "4":
            clear_screen()
            print("\n" + "="*70)
            print("SYSTEM INFORMATION")
            print("="*70)
            print(f"Max Failed Attempts: {rate_limiter.max_attempts}")
            print(f"Log File: {rate_limiter.log_file}")
            print(f"Registered Users: {len(rate_limiter.valid_credentials)}")
            print(f"Blocked Users: {len(rate_limiter.blocked_users)}")
            print(f"Active Failed Attempts: {len(rate_limiter.failed_attempts)}")
            print("="*70)
            input("\nPress Enter to continue...")
        
        elif choice == "5":
            rate_limiter.log_event(f"User '{username}' logged out")
            print("\n👋 Logging out...")
            return
        
        else:
            print("\n❌ Invalid choice!")
            input("\nPress Enter to continue...")


def main():
    """Main application."""
    rate_limiter = SimpleLoginRateLimiter(max_attempts=5)
    rate_limiter.log_event("System started")
    
    try:
        while True:
            username = login_screen(rate_limiter)
            dashboard(rate_limiter, username)
            
            clear_screen()
            print("\n" + "="*70)
            again = input("Login with different account? (yes/no): ").strip().lower()
            if again != 'yes':
                break
        
        clear_screen()
        print("\n👋 Thank you for using Secure Login System!")
        rate_limiter.log_event("System stopped normally")
        print()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted. Exiting...")
        rate_limiter.log_event("System interrupted")


if __name__ == "__main__":
    main()