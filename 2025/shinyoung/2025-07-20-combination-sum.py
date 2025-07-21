def combinationSum(candidates, target):
    result = []
    com = []

    nums = candidates

    n = len(nums)

    def dfs(i, cur_sum):
        if cur_sum == target:
            result.append(com[:])
            return

        if cur_sum > target or i == n:
            return

        dfs(i + 1, cur_sum)

        com.append(nums[i])
        dfs(i, cur_sum + nums[i])
        com.pop()

    dfs(0, 0)

    return result


print(combinationSum([2, 3, 6, 7], target=7))
