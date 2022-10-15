# 39. Combination Sum

> Problem link: https://leetcode.com/problems/combination-sum/  
> submission detail: https://leetcode.com/submissions/detail/822178279/  

```py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 중복되는 결과가 나오지 않게 하려면 분기되는 과정에서
        # 한쪽에서 추가한 candidate는 반대쪽에서 포함시키지 않아야 한다
        # [2]에서
        # [2, 2]가 된경우, 다른 트리 노드 에서는 2를 포함시키지 않아야 한다
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            # 같은 cantidate를 더한 케이스
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            # 같은 cantidate를 더하지 않은 케이스
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
```
