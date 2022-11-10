class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def add(a, b):
            return (a[0] + b[0], a[1] + b[1])
        
        def is_in_bound(pos):
            y, x = pos
            return y >= 0 and x >= 0 and y < r and x < c
        
        
        def get_next(pos, dir_i):
            cand = add(pos, dir_arr[dir_i])
            dir_cnt = 0
            while not is_in_bound(cand) or visited[cand[0]][cand[1]]:
                dir_i = (dir_i + 1) % 4
                dir_cnt += 1
                cand = add(pos, dir_arr[dir_i])
                if dir_cnt == 2:
                    return (pos, dir_i)
            return (cand, dir_i)
        
        
        r, c = len(matrix), len(matrix[0])
        visited = [[False] * c for _ in range(r)]
        dir_arr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_i = 0
        ret = []
        curr = (0, 0)
        (next_, dir_i) = get_next(curr, dir_i)
        while curr != next_:
            ret.append(matrix[curr[0]][curr[1]])
            visited[curr[0]][curr[1]] = True
            curr = next_
            (next_, dir_i) = get_next(curr, dir_i)
        ret.append(matrix[curr[0]][curr[1]])
        return ret
