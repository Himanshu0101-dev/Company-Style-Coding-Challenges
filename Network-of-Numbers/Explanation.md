123 -> 345 (digit 3)
345 -> 567 (digit 5)
Thus:
123, 345, 567 belong to one group.
890 is separate.
Largest group size = 3

# Example 
Input:
ids = [12, 34, 56, 78]
Output:
1

# Constraints 
1 <= ids.length <= 100000
1 <= ids[i] <= 10^9

# Expected approach 
# Observation
Each number contains digits from 0 to 9.
Instead of comparing every pair:
O(N²)
Create connections through digits.
# Example:
123 → {1,2,3}
345 → {3,4,5}
