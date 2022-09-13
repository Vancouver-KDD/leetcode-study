class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(arr):
            cnt = collections.Counter(arr)
            return sum(i != "." and cnt[i] > 1 for i in cnt) == 0
        
        if not board or not board[0]:
            return False
        for i in range(9):
            row = board[i]
            col = [board[x][i] for x in range(9)]
            sub = []
            for j in range(0, 9, 3):
                if i % 3 == 0:
                    sub = [board[y][x] for y in range(i, i+3) for x in range(j, j+3)]
                    if not is_valid(sub):
                        return False
            if not is_valid(row) or not is_valid(col):
                return False
        return True
