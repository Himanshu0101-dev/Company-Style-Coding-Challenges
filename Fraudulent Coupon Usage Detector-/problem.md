# Scenario: An e-commerce company notices users creating multiple accounts to repeatedly use "New User" coupons.
You need to build a system that detects suspicious accounts based on:
Same phone number used by multiple accounts
Same device ID used by multiple accounts
Same IP address used by many accounts
More than 3 accounts created within 24 hours from same device
# input 
accounts = [
  ("u1", "9876", "dev1", "1.1.1.1"),
  ("u2", "9876", "dev2", "1.1.1.2"),
  ("u3", "1234", "dev1", "1.1.1.3"),
  ("u4", "5678", "dev1", "1.1.1.4")
]

# output 
Suspicious Users:
u1, u2, u3, u4
