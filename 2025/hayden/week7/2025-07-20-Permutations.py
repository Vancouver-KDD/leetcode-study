# Question: Permutations (https://leetcode.com/problems/permutations/)

# Time Complexity: O(n * n!)
# Space Complexity: O(n!)

# Notes:
# - Use backtracking to generate all possible permutations.

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])
                return

            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return result
