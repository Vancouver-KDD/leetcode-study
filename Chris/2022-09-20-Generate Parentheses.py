class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        res = []
        # combo: current combination of parentheses
        # opening: number of opening parentheses currently being used
        # closing: number of closing parentheses currently being used
        def dfs(combo: str, opening: int, closing: int):
            
            if closing == n:
                res.append(combo)
                return
            
            if opening > closing:
                dfs(combo + ")", opening, closing+1)
                
            if opening < n:
                dfs(combo + "(", opening+1, closing)
            
        
        
        dfs("", 0, 0)
        
        return res
            