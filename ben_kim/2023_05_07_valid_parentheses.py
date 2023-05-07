class Solution:
    def valid_parentheses(self, s: str) -> bool:
        bracket_pair = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }

        stack = []
        for c in s:
            if c in bracket_pair: # 1
                stack.append(c)
            elif not stack or bracket_pair[stack.pop()] != c:
                return False
        
        return len(stack) == 0 # 2

# 1. `in` keyword is used to test for membership in a dictionary
# 2. edge case '['         