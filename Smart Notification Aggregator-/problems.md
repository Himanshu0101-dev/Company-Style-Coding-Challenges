A notification system receives events from different apps.
Each notification has:
userId
appName
timestamp
To avoid spamming users, notifications from the same app for the same user that occur within K seconds should be merged into a single notification batch.

# Input

notifications = [
("u1", "Instagram", 100),
("u1", "Instagram", 105),
("u1", "Instagram", 108),
("u1", "WhatsApp", 110),
("u1", "Instagram", 130)
]
 
K = 10
# Output
Plain Text
Instagram -> 2 batches
WhatsApp -> 1 batch
Explanation

Instagram:

100,105,108 → Same batch
130 → New batch

Total = 2

WhatsApp:

110 → One batch

Total = 1
# function signature 
def aggregate_notifications(notifications, k):
    pass

# constraints
1 <= N <= 100000
1 <= timestamp <= 10^9
