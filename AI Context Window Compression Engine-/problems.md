# Problem Statement
Design a system that compresses AI conversation history.
Given conversation messages:
[
    ("user", "My name is Himanshu"),
    ("assistant", "Nice to meet you"),
    ("user", "I work at Microsoft"),
    ...
]
and a token limit 
1000

Return the most relevant context while staying inside the limit.
Rules
Priority Order:
# Level 1
Always preserve:
User Profile Facts
Preferences
Goals
Memory Entries

# Example:
My name is Himanshu
I am preparing for Google interviews
I prefer Python

# Level 2
Keep recent messages.
Latest N messages
# Level 3
Summarize older conversations.
User discussed trees
User solved graph problem
User asked about DP
# level 4
delete irrevalant messages
hello
thanks
ok
nice
haha
# input 
messages
token_limit
# Output
Python
compressed_context
