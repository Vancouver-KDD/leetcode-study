
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        LEN = len(nums)
        def dfs(per):
            if len(per) == LEN:
                res.append(per.copy())
                return
            not_in = list(set(nums) - set(per))
            for i, elem in enumerate(not_in):
                per.append(elem)
                dfs(per)
                per.pop()        
        dfs([])
        return res
        
