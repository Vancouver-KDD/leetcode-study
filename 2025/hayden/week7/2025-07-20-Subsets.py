# Question: Subsets (https://leetcode.com/problems/subsets/)

# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

# Notes:
# - Use backtracking or iterative approach.
# - Generates all possible subsets (the power set).

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result
