class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m,n = len(board), len(board[0])
        wordLen = len(word)
        visit = set()
        
        def validIndices(a,b):
            return a >= 0 and b >= 0 and a < m and b < n
        
        def dfs(a, b, i):
            if i >= wordLen:
                return True
            if (a,b) in visit:
                return False
            
            if not validIndices(a,b) or word[i] != board[a][b]:
                return False
            visit.add((a,b))
            
            res = (dfs(a-1,b,i+1) or dfs(a+1,b,i+1) or dfs(a,b-1,i+1) or dfs(a,b+1,i+1))
            visit.remove((a,b))
            return res
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False
            
            
        
            