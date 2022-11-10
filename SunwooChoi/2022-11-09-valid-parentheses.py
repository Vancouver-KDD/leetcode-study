class Solution:
    def isValid(self, s: str) -> bool:
        # sets of left/right brackets
        left = {'(', '{', '['}
        right = {')', '}', ']'}
        
        # stack to store left parentheses
        stack = []
        
        for c in s:
            # if left bracket, stash
            if c in left:
                stack.append(c)
            else:
                # if right bracket, check it is matched with most recent bracket
                if len(stack) == 0 or not self.checkBracket(stack.pop(), c):
                    return False
        return stack == []
                    
    
    # check it is valid parentheses
    def checkBracket(self,left, right):
        validSet = {('(',')'), ('{','}'), ('[',']')}
        return (left, right) in validSet
       
 
