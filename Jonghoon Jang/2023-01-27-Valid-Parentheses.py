"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    # Sliding window
    # Time complexity: O(n): single pass at most once
    # Stack - push and pop:  O(1)
    # Space complexity: O(n): push all brackets to stack in the worst case
    def isValid(self, s: str) -> bool:
        stack = []

        p_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        for bracket in s:
            # open bracket
            if bracket in p_map:
                stack.append(bracket)

            # close bracket and corresponding open bracket is at the top of the stack
            elif bracket in p_map.values() and len(stack) != 0 and bracket == p_map[stack[-1]]:
                stack.pop()
            else:
                return False  # early exit

        return True


def main():
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))


if __name__ == "__main__":
    main()
