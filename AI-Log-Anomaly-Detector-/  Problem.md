# Problem Statement
A company uses an AI monitoring system that generates daily server health scores.

You are given an array health[] where:

health[i] represents the health score on day i.
A day is called anomalous if its score is strictly greater than both of its immediate neighbors.
Return all anomalous day indices.

# Example 1
Input
health = [40, 75, 50, 90, 60, 100, 80]
Output
[1, 3, 5]
# Explanation
health[1] = 75 > 40 and 50
health[3] = 90 > 50 and 60
health[5] = 100 > 60 and 80
Therefore, the anomalous indices are [1, 3, 5].

# Constraints
3 ≤ N ≤ 10^5
1 ≤ health[i] ≤ 10^9
Expected Complexity
Time Complexity: O(N)
Space Complexity: O(1)
Tags
Array, Simulation, Monitoring Systems, AI Analytics
