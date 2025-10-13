class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(num_set, arr):

            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for num in nums:

                if num not in num_set:
                    num_set.add(num)
                    arr.append(num)
                    dfs(num_set, arr)

                    num_set.remove(num)
                    arr.pop()

        dfs(set(), [])

        return res


# need to review