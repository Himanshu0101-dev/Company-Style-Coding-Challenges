# Problem Statement
Ek SaaS platform me hazaron users API requests bhejte hain.
Har user ke liye maximum K requests per T seconds allow hain.
Tumhe requests ki stream di jayegi:
# (user_id, timestamp)
Har request ke liye determine karo:
"ALLOW" → agar user limit ke andar hai
"BLOCK" → agar user ne already last T seconds me K requests kar li hain
# Example
# input 
k = 3
window = 10

requests = [
    ("u1", 1),
    ("u1", 2),
    ("u1", 3),
    ("u1", 4),
    ("u1", 12)
]
# output 
[
    "ALLOW",
    "ALLOW",
    "ALLOW",
    "BLOCK",
    "ALLOW"
]
# Explanation:
At timestamp 4, user u1 already made 3 requests in last 10 seconds.
At timestamp 12, timestamp 1 request expires, so request allowed.
# Expected Complexity
Time : O(N)
Space : O(N)
