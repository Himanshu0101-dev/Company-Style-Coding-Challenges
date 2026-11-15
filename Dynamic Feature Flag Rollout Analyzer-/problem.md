# problem statement 
A company rolls out a new feature to users gradually.
You are given:
users[i] → User ID
group[i] → Region/segment
successRate[i] → Success percentage after rollout
A rollout is considered stable if the difference between the maximum and minimum success rate in the selected contiguous user segment is at most K.
Return the length of the longest stable rollout window.
# Example
successRate = [85, 88, 90, 84, 87, 95]
K = 6
Window:
[85,88,90,84,87]
 max = 90
min = 84
 90 - 84 = 6
valid length = 5
Adding 95:
95 - 84 = 11
Invalid
# Output:
5
# Constraints
1 ≤ N ≤ 100000
0 ≤ successRate[i] ≤ 100
