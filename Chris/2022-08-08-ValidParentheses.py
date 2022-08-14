class Solution:
    def isValid(self, s: str) -> bool:
        
        openings = "([{"
        
        brackets = {}
        brackets[")"] = "("
        brackets["}"] = "{"
        brackets["]"] = "["
        
        stack = []
        
        
        for b in s:
            if b in openings:
                stack.append(b)
                
            else:
                # closing
                if len(stack) == 0 or b not in brackets or brackets[b] != stack.pop(): 
                    return False
                
        
        return len(stack) == 0
                
        
        
        