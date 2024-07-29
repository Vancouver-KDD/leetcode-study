class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        def backtracking(index):
            if index >= len(nums):
                result.append(subset[:])
                return

            subset.append(nums[index])
            backtracking(index+1)

            subset.pop()
            backtracking(index+1)
        backtracking(0)
        return result