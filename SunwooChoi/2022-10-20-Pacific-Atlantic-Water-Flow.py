class Solution:
    def find_path(self,visit:Set[Tuple[int]], row: int, col: int, heights: List[List[int]], prev_h: int) \
    -> None:
        # check current position is not out of boundary
        if row < 0 or row >= len(heights) or col < 0 or col >= len(heights[0]):
            return
        
        # check the current position is already visited
        if (row, col) in visit:
            return
        
        cur_h = heights[row][col]
        
        # check current position can be flowed to previous position
        if prev_h > cur_h:
            return
        
        visit.add((row, col))
        
        # dfs
        self.find_path(visit, row-1, col, heights, cur_h)
        self.find_path(visit, row+1, col, heights, cur_h)
        self.find_path(visit, row, col-1, heights, cur_h)
        self.find_path(visit, row, col+1, heights, cur_h)
        
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        # create 2D list to track accessibility to oceans
        access_pacific = set()
        access_atlantic = set()
        
        # iterate row
        for i in range(m):
            self.find_path(access_pacific, i, 0, heights, -1)
            self.find_path(access_atlantic, i, n-1, heights, -1)
        # iterate column
        for j in range(n):
            self.find_path(access_pacific, 0, j, heights, -1)
            self.find_path(access_atlantic, m-1, j, heights, -1)
        
        # return intersection of two set
        return [pos for pos in access_pacific if pos in access_atlantic]
