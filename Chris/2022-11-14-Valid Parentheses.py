class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {}
        
        brackets[')'] = '('
        brackets['}'] = '{'
        brackets[']'] = '['
        
        openings = "({["
        stack = []
        
        for c in s:
            if c in openings:
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() != brackets[c]:
                    return False
        
        return len(stack) == 0 
                
        
        
        