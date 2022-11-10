from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #i = pointer, cur = current variable (what value we added so far), total = total sum of the array.
        def dfs(i, cur, total):
            # base case
            if total == target:
                #We need to continuously use cur, therefore we don't want to modify it.
                res.append(cur.copy())
                return

            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            # recursive
            dfs(i+1, cur, total)
        dfs(0,[],0)
        return res


