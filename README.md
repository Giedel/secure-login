# Secure Login System v3.0

A professional console-based login system with rate limiting, security logging, and improved user experience.

## ✨ What's New in v3.0

- **Login-First Flow**: Must authenticate before accessing any features
- **Improved Dashboard**: Clean menu system after successful login
- **Better Unblock UI**: Shows all blocked users before unblocking
- **Enhanced Feedback**: Real-time security status and warnings
- **Multiple Users**: Support for multiple test accounts

## 🚀 Quick Start

```bash
# Run the simple version (recommended for testing)
python simple_secure_login.py

# Or run the enhanced version with password hashing
python secure_login_v3.py
```

## 🔑 Test Credentials

### Simple Version (`simple_secure_login.py`)
- **admin** / password123
- **user** / userpass
- **test** / test123

### Enhanced Version (`secure_login_v3.py`)
- **admin** / password123
- **user** / userpass

## 📋 How It Works

### 1. Login Screen
```
At startup, you'll see:
┌──────────────────────────────────────┐
│     🔐 SECURE LOGIN SYSTEM          │
├──────────────────────────────────────┤
│  Please enter your credentials       │
└──────────────────────────────────────┘

Username: [enter here]
Password: [enter here]
```

### 2. After Successful Login - Dashboard
```
┌──────────────────────────────────────┐
│         🔐 DASHBOARD                │
│  Logged in as: admin                 │
│  Time: 2025-11-20 01:13:29          │
├──────────────────────────────────────┤
│  📋 MAIN MENU                        │
│  1. 📊 View Security Status          │
│  2. 📄 View Security Logs            │
│  3. 🔓 Unblock User                  │
│  4. ℹ️  System Info                  │
│  5. 🚪 Logout                        │
└──────────────────────────────────────┘
```

## 🎯 Features

### 1. View Security Status
Shows:
- Currently blocked users with attempt counts
- Users with failed attempts (not yet blocked)
- System configuration

### 2. View Security Logs
Displays:
- Last 30 log entries with timestamps
- All login attempts (successful and failed)
- Block/unblock events
- System start/stop events

### 3. Unblock User
**NEW**: Shows list of blocked users before asking which to unblock!
```
🚫 Currently Blocked Users (2):
──────────────────────────────────────
  1. hacker - Failed attempts: 5
  2. attacker - Failed attempts: 7
──────────────────────────────────────
Enter username to unblock: [type here]
```

### 4. System Info
Shows system configuration and statistics

## 🧪 Testing Scenarios

### Test 1: Successful Login
1. Run the program
2. Enter: `admin` / `password123`
3. ✅ Should see dashboard

### Test 2: Failed Login Attempts
1. Run the program
2. Enter: `admin` / `wrongpass`
3. ⚠️ Should see warning with remaining attempts
4. Check Security Logs to see it was logged

### Test 3: Account Lockout
1. Run the program
2. Fail login 5 times with same username
3. 🚫 Account gets blocked
4. Try again - blocked message appears
5. Check Security Logs for SECURITY ALERT

### Test 4: Unblock User
1. First, block a user (fail 5 times)
2. Login with different account
3. Go to Menu option 3 (Unblock User)
4. See the blocked user in the list
5. Enter username to unblock
6. ✅ User is unblocked

### Test 5: Multiple Users
1. Login as `admin`
2. Logout
3. Login as `user`
4. Each user's sessions are logged separately

## 📊 Log File Format

`security_log.txt` contains entries like:
```
[2025-11-20 01:13:29] System started
[2025-11-20 01:13:45] Failed login attempt for 'admin' (Attempt 1/5)
[2025-11-20 01:14:01] Successful login for user 'admin'
[2025-11-20 01:14:30] User 'admin' logged out
[2025-11-20 01:15:12] Failed login attempt for 'hacker' (Attempt 5/5)
[2025-11-20 01:15:12] SECURITY ALERT - User 'hacker' blocked after 5 failed attempts
[2025-11-20 01:16:00] User 'hacker' was unblocked
```

## 🔒 Security Features

✅ **Rate Limiting**: 5 attempts max before block  
✅ **Audit Trail**: All events logged with timestamps  
✅ **User Feedback**: Clear warnings before lockout  
✅ **Block Persistence**: Enhanced version saves blocks to file  
✅ **Password Protection**: Enhanced version uses SHA-256 hashing  

## 📁 Files

- `simple_secure_login.py` - Easy to test, plain text passwords
- `secure_login_v3.py` - Production-ready with hashing
- `security_log.txt` - Auto-generated log file
- `login_data.json` - Persistent storage (enhanced version only)

## 🎨 UI Improvements

- ✅ Clear screen between sections
- ✅ Emoji indicators for better readability
- ✅ Consistent formatting throughout
- ✅ Real-time timestamp displays
- ✅ Blocked users list before unblocking
- ✅ Helpful hints and test credentials shown

## 💡 Usage Tips

1. **Start Simple**: Use `simple_secure_login.py` for testing
2. **Test Blocking**: Use a fake username to test without blocking real accounts
3. **Check Logs**: View logs after each test to see what was recorded
4. **Unblock Testing**: Block a user, then practice unblocking them
5. **Multiple Sessions**: Logout and login with different accounts

## ⚠️ Production Notes

For real-world use, consider:
- Use environment variables for credentials
- Implement time-based auto-unblock
- Add database instead of in-memory storage
- Use bcrypt/argon2 instead of SHA-256
- Add session tokens
- Implement IP-based rate limiting
- Add email notifications

## 🆘 Troubleshooting

**Problem**: Can't see menu after login  
**Solution**: Make sure you pressed Enter after successful login

**Problem**: Blocked users not showing in unblock menu  
**Solution**: You need to block a user first (fail 5 times)

**Problem**: Log file not found  
**Solution**: It's created on first log event, try logging in first

## 📝 Changelog

### v3.0 (Current)
- Login-first flow
- Dashboard after authentication
- Blocked users list in unblock menu
- Improved UI/UX
- Better error messages

### v2.0
- Added password hashing
- Persistent storage
- Enhanced security

### v1.0
- Basic rate limiting
- Security logging
- Console interface

---

**Created for**: Educational and demonstration purposes  
**Last Updated**: 2025-11-20
```