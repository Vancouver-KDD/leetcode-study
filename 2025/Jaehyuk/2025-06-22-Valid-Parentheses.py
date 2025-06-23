class Solution:
    def isValid(self, s:str) -> bool:
        stack = []
        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
            else:
                if not stack:
                    return False
                check = stack.pop()
                if check == "(":
                    if p != ")":
                        return False
                elif check == "{":
                    if p != "}":
                        return False
                elif check == "[":
                    if p != "]":
                        return False
        return not stack
    