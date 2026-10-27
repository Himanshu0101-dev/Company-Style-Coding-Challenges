# Problem Statement
An AI company processes user requests.
Each request requires a certain number of tokens.
A model can process at most K tokens in one batch.
Given token requirements of N requests, find the minimum number of batches needed.
A batch can contain multiple requests as long as their total token count does not exceed K.

# Example 
N = 6
tokens = [3, 5, 2, 4, 1, 6]
K = 7
# Possible batches:
(6,1)
(5,2)
(4,3)
# Answer:
3
# input 
N
K
tokens[0...N-1

# output
minimum number pf batches 

# Constraints 
1 <= N <= 100000
1 <= tokens[i] <= K <= 100000

# Idea
This is similar to how AI serving systems try to maximize context-window utilization.
Use:
Sort requests
Smallest + Largest together
If fit, batch them
Otherwise largest alone
This minimizes batch count.
