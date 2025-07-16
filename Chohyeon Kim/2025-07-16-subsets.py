class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(index: int, arr):

            if index >= len(nums):
                res.append(arr.copy())
                return

            nt_arr = arr

            nt_arr.append(nums[index])
            dfs(index + 1, nt_arr)
            nt_arr.pop()
            dfs(index + 1, nt_arr)

        dfs(0, [])

        return res
