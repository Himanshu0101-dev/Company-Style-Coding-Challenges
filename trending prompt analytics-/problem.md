# Problem Statement
An AI platform logs prompts submitted by users.
prompts = [
    "ai",
    "code",
    "ai",
    "chatbot",
    "code",
    "ai"
]
Return the top k most frequent prompts.
If two prompts have the same frequency, return them in lexicographical order.

# example 1 
# Input:
prompts = ["ai","code","ai","chatbot","code","ai"]
k = 2
# Output:
["ai","code"]

# Explanation:
ai -> 3 code -> 2 chatbot -> 1
Top 2 frequent prompts:


# exmaple 
# Input:
 
prompts = ["z","a","b","a","b"]
k = 2
 
Output:
 
["a","b"]

Explanation:
a -> 2
b -> 2
z -> 1
