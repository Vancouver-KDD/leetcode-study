class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # total num of ( or ) can not be bigger than n
        
        res = []
        
        def dfs(tmp, l, r):
            # the num of ) can not be bigger than (
            if l == r == n:
                res.append(tmp)
            
            if l < n and r <= n:
                dfs(tmp+'(', l+1, r)
            if l != 0 and l > r and l <= n and r < n:
                dfs(tmp+')', l, r+1)
        
        dfs("",0,0)
        
        return res
        