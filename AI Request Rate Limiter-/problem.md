# Problem Statement
A cloud AI platform receives API requests from users.
You are given an array requests where:
requests[i] = [timestamp, userId]
Timestamps are in increasing order.
A user is considered rate-limited if they make more than k requests within any rolling window seconds.
Return the list of users who violated the rate limit at least once.
# example 
requests = [
    [1, "A"],
    [2, "A"],
    [3, "A"],
    [5, "B"],
    [6, "B"],
    [7, "B"]
]

k = 2
window = 3
# explanation 
USER a:
1,2,3
Within 3 seconds there are 3 requests.
Violation ✅
USER b:
5,6,7
Within 3 seconds there are 3 requests.
Violation ✅

# Output:
["A","B"]

# optimal approach
For each user:

Store request timestamps.
Maintain a sliding window.
Remove timestamps outside the current window.
If window size exceeds k, mark the user as violating.

# complexity 
Time: O(n)
Space: O(n)
