# KDD LeetCode Study Week 3: Stack
# Assignment 3
# Title: Daily Temperatures
# Author: Youngjoon Park
# Date: 2025-06-17
# URL: https://leetcode.com/problems/daily-temperatures

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day
            
            stack.append(i)
        
        return answer
