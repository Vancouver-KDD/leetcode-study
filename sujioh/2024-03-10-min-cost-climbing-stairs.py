# Input: cost = [10,15,20]
# [10, 15, 20, 1, 2]
# [10, 15, 30, 16, 17]
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = []
        dp.append(cost[0])
        dp.append(cost[1])
        n = len(cost)
        for i in range(2, n):
            dp.append(cost[i] + min(dp[i-1], dp[i-2]))

        return min(dp[n-1], dp[n-2])

cost = [1,100,1,1,1,100,1,1,100,1]
# dp = [1,100,2,3,3,103,4,5,105,6] 
s = Solution()
s.minCostClimbingStairs(cost)

'''SUMMARY
Category: DP 

Let's consider the given array cost = [10, 15, 20].
We want to find the minimum cost to reach the top of the floor.
We can start from either the step with index 0 or the step with index 1.

Here's the breakdown of how the code works with this example:
Initialize dp = [10, 15], 
representing the minimum cost to reach the first and second steps.

Iteration starts from the third step:
For the third step (i = 2), the cost is cost[2] = 20. 
To reach step 2, we either come from step 1 with cost dp[1] = 15 or from step 0 with cost dp[0] = 10. 
So, the minimum cost to reach step 2 is min(dp[1], dp[0]) + cost[2] = min(15, 10) + 20 = 30.

At the end of the iteration, dp = [10, 15, 30].
Finally, the code returns the minimum cost to reach the top floor,
which is the minimum of the cost of the last step (dp[n-1] = dp[2] = 30)
'''