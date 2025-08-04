# Question: Combination Sum (https://leetcode.com/problems/combination-sum/)

# Time Complexity: O(2^t)  (t = target)
# Space Complexity: O(target)

# Notes:
# - Use backtracking.
# - Elements can be reused unlimited times.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # not i + 1 because we can reuse same element
                path.pop()

        backtrack(0, [], 0)
        return result
