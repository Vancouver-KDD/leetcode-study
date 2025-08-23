# KDD LeetCode Study Week 12: Graph(BFS/DFS/Union)
# Assignment 3
# Author: Youngjoon Park
# URL: https://leetcode.com/problems/number-of-islands

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        islands = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        
        return islands
