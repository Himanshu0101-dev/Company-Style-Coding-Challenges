# Problem Statement
An AI company serves thousands of LLM (Large Language Model) requests every second.
Each request arrives at a specific time and requires a certain amount of GPU processing time.
A GPU can process only one request at a time.
Given a list of requests, determine the minimum number of GPUs required so that no request has to wait.

# input 
requests = [
    [1, 4],
    [2, 5],
    [7, 9],
    [3, 6]
]
# output 
3

# explanation 
GPU1 : [1,4] -> [7,9]
GPU2 : [2,5]
GPU3 : [3,6]

# constraints
1 <= n <= 100000
1 <= start < end <= 10^9

# approach 
Sort requests by start time.
Use a Min Heap to track GPU release times.
If the earliest GPU becomes free before the next request arrives, reuse it.
Otherwise allocate a new GPU.
Heap size at the end gives the minimum GPUs required.
