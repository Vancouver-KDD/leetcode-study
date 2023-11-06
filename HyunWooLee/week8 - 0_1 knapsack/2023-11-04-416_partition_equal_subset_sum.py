class Solution:
    def canPartitionDfs(self, nums: List[int]) -> bool:

        def dfs(index, curr_sum):

            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            if len(nums) == index:
                return False

            if curr_sum == target:
                return True
            elif curr_sum > target:
                return False

            take = dfs(index + 1, curr_sum + nums[index])
            skip = dfs(index + 1, curr_sum)

            result = take or skip
            memo[(index, curr_sum)] = result
            return result

        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total / 2

        memo = {}

        return dfs(0, 0)