# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        # for this problem we can use a stack as stacks are last-in-first-out (LIFO)
        # we can map the bracket pairs and create a stack to store the the right brackets and pop the bracket off the stack as a match is found
        # if there is no match but the stack is empty or if the bracket at the top of the stack is not a match, we can return False, else True

        bracket_map = {"(": ")", "{": "}", "[": "]"}
        bracket_stack = []

        for bracket in s:
            if bracket in bracket_map:
                bracket_stack.append(bracket)
            else:
                if bracket_stack == [] or bracket_map[bracket_stack.pop()] != bracket:
                    return False

        if bracket_stack != []:
            return False
        else:
            return True
