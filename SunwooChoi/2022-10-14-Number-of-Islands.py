class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # find the island
                if grid[row][col] == "1":
                    num_island += 1
                    self.backTrackLands(grid, row, col)
        return num_island

    # mark all land elements of the current island
    def backTrackLands(self, grid: List[List[str]], row: int, col:int) -> None:
        # check out of boundary
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        # if current element is a land, keep marking adjacent elements
        if grid[row][col] == "1":
            grid[row][col] = "2"
            self.backTrackLands(grid, row+1, col)
            self.backTrackLands(grid, row-1, col)
            self.backTrackLands(grid, row, col+1)
            self.backTrackLands(grid, row, col-1)