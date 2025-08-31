# KDD LeetCode Study Week 12: Graph(BFS/DFS/Union)
# Assignment 2
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/pacific-atlantic-water-flow

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        
        def dfs(i, j, visited, prev_height):
            if (i < 0 or i >= m or j < 0 or j >= n or 
                (i, j) in visited or heights[i][j] < prev_height):
                return
            
            visited.add((i, j))
            
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in directions:
                dfs(i + di, j + dj, visited, heights[i][j])
        
        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
        for j in range(n):
            dfs(0, j, pacific, heights[0][j])
        
        for i in range(m):
            dfs(i, n-1, atlantic, heights[i][n-1])
        for j in range(n):
            dfs(m-1, j, atlantic, heights[m-1][j])
        
        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])
        
        return result
