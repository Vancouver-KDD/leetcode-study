class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        letters = "abcdefghijklmno"                 
        digitMap = {}
        
        for i in range(2,7):
            digitMap[i] = letters[(i-2)*3:(i-2)*3+3]
        digitMap[7] = "pqrs"
        digitMap[8] = "tuv"
        digitMap[9] = "wxyz"
        
        
        res = []
        
        def dfs(digits, combo):
            if len(digits) == 0:
                res.append(combo)
                return
            
            chars = digitMap[int(digits[0])]
            
            for c in chars:
                newCombo = combo + c
                dfs(digits[1:],newCombo)
        
        dfs(digits, "")
        
        return res
                
                
            
            
        
        
        
        