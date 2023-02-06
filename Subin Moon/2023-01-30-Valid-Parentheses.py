"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false
"""

class Solution:
    # Solution 1: Using Stack
    def isValid(self, s: str) -> bool:
        pair = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char not in pair:
                stack.append(char)
            elif not stack or pair[char] != stack.pop():
                return False

        return len(stack) == 0
