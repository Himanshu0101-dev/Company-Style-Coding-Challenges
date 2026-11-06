# Problem Statement
A tech company is rolling out multiple AI features. Some features depend on others being released first.
You are given:
n features numbered from 0 to n-1
A list of dependencies dependencies[i] = [a, b]
meaning feature a can only be released after feature b
Your task is to:
Determine if all features can be released.
If possible, return one valid release order.
If there is a cyclic dependency, return an empty list.
# example 1 
# Input:
n = 4
dependencies =
[
 [1,0],
 [2,0],
 [3,1],
 [3,2]
]
Output:
[0,1,2,3]
# explanation
0 must come before 1 and 2
1 and 2 must come before 3
# example 2 
Input:
n = 3
dependencies =
[
 [0,1],
 [1,2],
 [2,0]
]
Output:
[]
# explanation
Cycle exists:
0 → 1 → 2 → 0
