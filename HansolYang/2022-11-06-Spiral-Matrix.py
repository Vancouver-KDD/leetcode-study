class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        n = len(matrix)
        m = len(matrix[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr = (0,0)
        res = []
        
        def get_next(pos, direc):
            curr_dindex = directions.index(direc)
            for i in range(4):
                if is_valid((pos[0]+direc[0], pos[1]+direc[1])):
                    return ((pos[0]+direc[0], pos[1]+direc[1]), direc)
                else:
                    direc = directions[(curr_dindex + 1) % 4]
            return (pos, direc)
        
        def is_valid(pos):
            return (0 <= pos[0] <= n-1) and (0 <= pos[1] <= m-1) and (visited[pos[0]][pos[1]] != True)
        
        curr_d = directions[0]
        next_ = get_next(curr, curr_d)[0]
        
        
        while curr != next_:
            res.append(matrix[curr[0]][curr[1]])
            visited[curr[0]][curr[1]] = True
            curr = next_
            next_ = get_next(curr, curr_d)[0]
            curr_d = get_next(curr, curr_d)[1]
        
        res.append(matrix[next_[0]][next_[1]])
            
        return res