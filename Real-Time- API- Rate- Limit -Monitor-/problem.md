# company context 
Modern platforms like Stripe, Uber, Swiggy, Zomato, and Microsoft monitor API traffic continuously.
Given a stream of API requests represented by user IDs, determine the first user who exceeds a rate limit of K requests.

# problem statement 
Modern applications monitor API traffic to prevent abuse.
You are given:
requests[i] representing a user making an API request
Integer K representing the maximum allowed requests
Return the first user who exceeds K requests.

If no user exceeds the limit return -1.

# Example
Input

requests = [101,102,101,103,101,102,101]
K = 3
Output

101
# Constraints
1 ≤ N ≤ 100000
1 ≤ requests[i] ≤ 10^9
1 ≤ K ≤ 10000
# Expected Complexity
Time: O(N)
Space: O(N)
Tags
HashMap, Streaming Data, Rate Limiting, Backend Engineering
