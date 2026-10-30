# Problem Statement
A payment gateway monitors transactions in real time.
A user is flagged if they perform more than K transactions within any window of T minutes.
Given a list of transactions represented as:
(userId, timestamp)
Return the first user ID that violates the limit.
Return -1 if no violation exists.

# Example
# Input
transactions = [
(101,1),
(102,2),
(101,3),
(101,5),
(102,6),
(101,8)
]

K = 3
T = 10
# Output
101

# Constraints
1 <= N <= 100000
1 <= userId <= 10^9
1 <= timestamp <= 10^9
1 <= K <= 1000
1 <= T <= 100000
# Expected Complexity
# Time Complexity: O(N)
# Space Complexity: O(N)
# Tags
HashMap, Queue, Sliding Window, FinTech, Fraud Detection
