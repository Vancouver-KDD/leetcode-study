class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        1. goes from ocean to cells until it's possible and stores a cell while go through
            vertically and horizontally
        2. create dict or set to log each cell connected with Ocean
        3. find the cell that belongs to both Ocean and return it
        
        """
        
        ROWS = len(heights)
        COLS = len(heights[0])
        
        pacific, atlantic = set(), set()
        res = []
        
        def dsf(r, c, visit, prevCell):
            if ((r, c) in visit 
                or r < 0 or c < 0 
                or r == ROWS 
                or c == COLS
                or heights[r][c] < prevCell 
               ):
                return
            visit.add((r,c))
            dsf(r + 1,c,visit, heights[r][c])
            dsf(r - 1,c,visit, heights[r][c])
            dsf(r,c + 1,visit, heights[r][c])
            dsf(r,c - 1,visit, heights[r][c])

        
        for c in range(COLS):
            dsf(0, c, pacific, heights[0][c])
            dsf(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
            
        for r in range(ROWS):
            dsf(r, 0, pacific, heights[r][0])
            dsf(r, COLS - 1, atlantic, heights[r][COLS - 1])
            
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res