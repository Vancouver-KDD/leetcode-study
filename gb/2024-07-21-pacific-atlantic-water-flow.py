2j


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacificSet = set()
        atlanticSet = set()

        # set pacific
        # start from first row
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(r, c, oceanSet, prev, visit):
            if r not in range(ROWS) or c not in range(COLS) or heights[r][c] < prev or (r, c) in visit:
                return
            visit.add((r, c))
            oceanSet.add((r, c))
            for dr, dc in directions:
                dfs(dr+r, dc+c, oceanSet, heights[r][c], visit)

        for c in range(COLS):
            visit = set()
            dfs(0, c, pacificSet, 0, visit)

        for r in range(1, ROWS):
            visit = set()
            dfs(r, 0, pacificSet, 0, visit)
        # setAtlantic

        for c in range(COLS):
            visit = set()
            dfs(ROWS-1, c, atlanticSet, 0, visit)

        for r in range(ROWS-1):
            visit = set()
            dfs(r, COLS-1, atlanticSet, 0, visit)

        print("list(pacificSet and atlanticSet): ",
              list(pacificSet & atlanticSet))
        return list(pacificSet & atlanticSet)
