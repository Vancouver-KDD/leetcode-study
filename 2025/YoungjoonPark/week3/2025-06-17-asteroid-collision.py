# KDD LeetCode Study Week 3: Stack
# Assignment 2
# Title: Asteroid Collision
# Author: Youngjoon Park
# Date: 2025-06-17
# URL: https://leetcode.com/problems/asteroid-collision

from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for asteroid in asteroids:
            if asteroid < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                
                if stack and stack[-1] == abs(asteroid):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
        
        return stack