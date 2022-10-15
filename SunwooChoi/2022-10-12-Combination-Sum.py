class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        self.dfs(target, candidates, [], ans, 0)
        return ans
        
    # depth first search with back tracking from idx to len(candidate) 
    def dfs(self, target: int, candidates: List[int], cur: List[int], ans: List[List[int]], idx: int) -> None:
        # find the answer
        if target == 0:
            ans.append(cur.copy()) # create new copy of list (not cur's reference)
            return
        # back tracking from idx to last element of candidates
        for i in range(idx, len(candidates)):
            if target < candidates[i]:
                continue
            cur.append(candidates[i])
            self.dfs(target-candidates[i], candidates, cur, ans, i)
            cur.pop()