# Scenario (Real Company Issue):
 At companies like Microsoft, Capgemini, Indian Oil, Amazon, and Flipkart, APIs have request limits.
 If too many requests come from a client in a short time, the API should be blocked temporarily.

 # problem
 Given a list of API requests:
(userId, timestamp)
A user can make at most 5 requests within any 60-second window.
Return all user IDs that violated the rate limit.
# example
requests = [
    ("A", 1),
    ("A", 10),
    ("A", 20),
    ("A", 30),
    ("A", 40),
    ("A", 50),
    ("B", 1),
    ("B", 70),
    ("B", 140)
]
# output
["A"]
