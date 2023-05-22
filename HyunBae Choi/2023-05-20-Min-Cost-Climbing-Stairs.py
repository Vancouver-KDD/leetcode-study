# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

#    we will use dynamic programming and work from the back (bottom-up)
# 1. append a 0 to the end of the array to rid of index out of bounds error
# 2. loop through in range of the height of the decision tree minus 3, since we want the last the value at the second last index,
#    we will loop through until the end of the array from the back by decrementing by 1 (range(len(cost) - 3, -1 (from the back), -1 (decrementing by 1)))
# 3. update the cost at index i to be equal to cost at index i plus the minimum cost between taking 1 step or taking 2 steps
# 4. return the minimum between cost at index 0 and 1

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2]) # either single or double jump
        
        return min(cost[0], cost[1])
