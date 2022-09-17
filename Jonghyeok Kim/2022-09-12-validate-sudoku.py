class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Init dict where key is the index, value is the set of number
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sq = collections.defaultdict(set)
        
        for c in range(9):
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in cols[c] 
                    or board[r][c] in cols[r]
                    or board[r][c] in sq[(r//3, c//3)]):
                    return False
                else:
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    sq[r//3, c//3].add(board[r][c])
        return True