# 20. Valid Parentheses

> Problem link: https://leetcode.com/problems/valid-parentheses/  
> submission detail: https://leetcode.com/submissions/detail/758591310/  

```py
class Solution:
    def isValid(self, s: str) -> bool:

        parentheses_pair = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        open_parentheses = parentheses_pair.keys()
        close_parentheses = parentheses_pair.values()
        temp_arr = []

        for char in s:
            if char in close_parentheses:
                if temp_arr and parentheses_pair[temp_arr[-1]] == char:
                    temp_arr.pop()
                else:
                    return False

            else:
                temp_arr.append(char)
            
        return True if not temp_arr else False
```