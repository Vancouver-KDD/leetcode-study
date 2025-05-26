from typing import List

# [9,2,2,4,6,1,5]
# [1,2,2,4,5,6,9]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output_list = []

        def dfs(i, cur, total):
            if total == target:
                output_list.append(cur.copy())
                return
            if total > target or i == len(candidates):
                return

            # include candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            # skip candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return output_list


solution = Solution()
output = solution.combinationSum2([9,2,2,4,6,1,5], 8)
print(output)
