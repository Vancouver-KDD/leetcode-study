class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                stk.append(i)
            else:
                if not stk or (i == "}" and stk[-1] != "{") or \
                (i == "]" and stk[-1] != "[") or \
                (i == ")" and stk[-1] != "("):
                    return False
                stk.pop()
        return len(stk) == 0
