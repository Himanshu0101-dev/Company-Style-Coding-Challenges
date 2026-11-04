# Problem Statement
A company has N AI models waiting for deployment.
For each model:
deployTime[i] = time required to deploy the model.
deadline[i] = latest acceptable deployment completion time.
Only one model can be deployed at a time.
Find the maximum number of AI models that can be deployed before their deadlines.
# example 1 
# Input:
deployTime = [3,2,4,1]
deadline   = [5,6,8,3]
# Output:
3
# explanation 
Deploy Model 4 (1 hour) → finishes at 1
Deploy Model 2 (2 hours) → finishes at 3
Deploy Model 1 (3 hours) → finishes at 6 ❌
Instead:
Deploy Model 4 → 1
Deploy Model 1 → 4
Deploy Model 2 → 6 ✅
Total = 3 models
# constraints 
1 <= N <= 100000
1 <= deployTime[i] <= 10000
1 <= deadline[i] <= 1000000

# optimal approach
Greedy + Max Heap
Sort models by deadline.
Add deployment times one by one.
Keep track of total deployment time.
If total time exceeds current deadline:
Remove the model with largest deployment time.
Heap size = answer.

# complexity 
Time: O(N log N)
Space: O(N)
