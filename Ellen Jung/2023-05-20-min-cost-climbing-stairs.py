class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) == 1:
            return cost[0]
        elif len(cost) == 2:
            return min(cost[0], cost[1])
        elif len(cost) == 3:
            return min(cost[0] + cost[2], cost[1])

        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
        return min(cost[-2],cost[-1])