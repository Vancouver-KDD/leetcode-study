class Solution:
    def min_cost_climbing_stairs(self, cost: list[int]) -> int:
        for i in range(len(cost) - 3, -1, -1): # range(start, stop, step), stop index is not included in this iteration loop
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
    

solution = Solution()
list1 = [10, 15, 20]
list2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(solution.min_cost_climbing_stairs(list1))
print(solution.min_cost_climbing_stairs(list2))