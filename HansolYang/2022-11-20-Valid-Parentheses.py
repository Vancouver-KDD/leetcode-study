class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        
        def check_match(p, q):
            return (p == "(" and q == ")") or (p == "[" and q == "]") or (p == "{" and q == "}")
        
        for i in s:
            if i in "([{":
                stk.append(i)
            else:
                if len(stk) > 0 and check_match(stk[-1], i):
                    stk.pop()
                else:
                    return False
        
        return len(stk) == 0
                    