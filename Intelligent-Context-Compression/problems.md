# Problem Statement
An AI chatbot has a maximum context window of K tokens.
You are given a conversation represented as an array tokens[], where:tokens[i] = number of tokens used by message i
Messages must remain in order.
To fit into the context window, the AI may remove some messages.
The AI wants to keep the longest continuous sequence of messages whose total tokens do not exceed K.
Find the maximum number of consecutive messages that can be kept.

# EXAMPLE 1
tokens = [120, 80, 150, 100, 50]
K = 300
Possible valid windows:
[120,80] = 200
[80,150] = 230
[150,100,50] = 300
Maximum length = 3
Output:
Plain Text
3

# Example 2 
tokens = [50,50,50,50]
K = 100
Output : 2

# Constraints
1 ≤ n ≤ 10^5
1 ≤ tokens[i] ≤ 10^9
1 ≤ K ≤ 10^15
