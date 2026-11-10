# Problem Statement
Modern AI companies gradually release features to users using Feature Flags.
Given:
enable feature_name percentage
disable feature_name
query user_id

A user gets a feature if:
hash(user_id + feature_name) % 100 < percentage
and the feature is currently enabled.
Return all enabled features for each queried user, sorted alphabetically.
# example 
# input 
operations = [
    ["enable", "AI_Search", "30"],
    ["enable", "SmartReply", "50"],
    ["query", "1001"],
    ["disable", "AI_Search"],
    ["query", "1001"]
]
# output
[
    ["SmartReply"],
    ["SmartReply"]
]
# complexity 
Enable  : O(1)
Disable : O(1)
Query   : O(F)

F = active features
