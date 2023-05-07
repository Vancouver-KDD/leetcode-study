class Solution:
    def isValid(self, s: str) -> bool:

        paren_dict = {")":"(","}":"{","]":"["}
        stack = []

        for char in s:
            # char is closing parentheses
            if char in paren_dict:
                if not stack or stack[-1] != paren_dict[char]:
                    return False
                else:
                    stack.pop()

            # char is opening parentheses
            else:
                stack.append(char)

        return not stack

    # Time complexity: o(n)
    # Space complexity: o(n)
    