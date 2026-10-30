# Problem Statement
Modern software companies release features gradually.
Given a list of user IDs and a rollout percentage, determine which users should receive the new feature.

Rule:
(userId % 100) < rolloutPercentage
Return true if feature is enabled, otherwise return false.

# Example
# Input
userIds = [101,205,310,450]
rolloutPercentage = 20

# Output
[true,true,true,false]

# Constraints
1 <= N <= 100000
1 <= userId <= 10^9
0 <= rolloutPercentage <= 100
# Expected Complexity
# Time Complexity: O(N)

# Space Complexity: O(N)
# Tags
Hashing, Simulation, Backend Engineering, Feature Flags, Product Systems
