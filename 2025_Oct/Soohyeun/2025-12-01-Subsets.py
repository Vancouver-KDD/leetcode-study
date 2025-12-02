class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(subset, index):
            res.append(subset[:])

            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtracking(subset, i + 1)
                subset.pop()

        backtracking([], 0)
        return res
