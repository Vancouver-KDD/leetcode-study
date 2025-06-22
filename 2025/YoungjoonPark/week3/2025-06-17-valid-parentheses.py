# KDD LeetCode Study Week 3: Stack
# Assignment 1
# Title: Valid Parentheses
# Author: Youngjoon Park
# Date: 2025-06-17
# URL: https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        for i in range(0, len(s)):
            if s[i] in pairs:
                stack.append(s[i])
            elif len(stack) == 0 or s[i] != pairs[stack.pop()]:
                return False

        return len(stack) == 0
