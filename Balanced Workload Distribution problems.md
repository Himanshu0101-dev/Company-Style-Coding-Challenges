Given an array hours[] representing project hours, divide projects between two teams such that the absolute difference between total hours assigned to each team is minimized.

# Example

Input:
hours = [3, 1, 4, 2, 2]
 
Output:
0
 
Explanation:
Team A = {3, 2}
Team B = {4, 2, 1}
 
Both teams get 5 hours.
Difference = 0

# Complexity Goal

Time: O(n * sum)
Space: O(sum)
