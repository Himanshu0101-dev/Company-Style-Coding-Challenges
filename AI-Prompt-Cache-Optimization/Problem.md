# Problem Statement

Modern AI assistants process millions of prompts daily. To reduce costs, identical prompts are cached.
You are given an array of user prompts represented as strings.
Two prompts belong to the same cache group if they contain exactly the same words irrespective of order.
Determine the maximum number of prompts that can be served from a single cache group.

# Example

# Input
5
ai tools future
future ai tools
machine learning rocks
rocks learning machine
ai tools future
# output 
3

# Explanation
# The prompts
ai tools future
future ai tools
ai tools future
all belong to the same cache group.
Hence answer = 3.

# Constraints
1 ≤ N ≤ 100000
1 ≤ Length(prompt) ≤ 100

# Approach
Each prompt is normalized by:
Split into words
Sort words
Join back into a canonical string
Now count frequency of every canonical string.
The highest frequency is the answer.

# Complexity 
Time: O(N × K log K)
K = number of words in a prompt
