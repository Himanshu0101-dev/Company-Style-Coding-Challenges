# Problem Statement
Large Language Models have limited context windows.
You are given a sequence of messages in a conversation.
Each message has:
tokens[i] → token count
importance[i] → importance score
You have a maximum context budget K.
Select messages whose total tokens do not exceed K while maximizing total importance.
Return the maximum importance achievable.
# example
tokens = [50,40,60,30]
importance = [100,60,120,50]
K = 100
possible selections:
50 + 40 = 90 tokens
importance = 160

60 + 30 = 90 tokens
importance = 170
170
# Before sending context to an LLM:
Conversation
↓
Important Messages Selection
↓
Context Window
↓
LLM
# expected complexity 
O(N * K)
