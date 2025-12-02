class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(start):
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtracking(start + 1)
                nums[i], nums[start] = nums[start], nums[i]

        backtracking(0)
        return res
