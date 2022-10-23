def wallsAndGates(self, rooms: List[List[int]]) -> None:
	def dfs(rooms, r, c, d):
            for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                if 0 <= r+x < len(rooms) and 0 <= c+y < len(rooms[0]) and rooms[r+x][c+y] > rooms[r][c]:
                    rooms[r+x][c+y] = d + 1
                    dfs(rooms, r+x, c+y, d+1)     
    if not rooms:
        return []

    for r in range(len(rooms)):
        for c in range(len(rooms[0])):
            if rooms[r][c] == 0:
                dfs(rooms, r, c, 0)