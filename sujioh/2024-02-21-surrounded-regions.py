class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.COLS = len(board[0])
        self.ROWS = len(board)
        visit = set()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if r == 0 or r == self.ROWS -1 or c == 0 or c == self.COLS -1:
                    self.unsurrounded_cell_marker(board, r, c, visit)

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

    def unsurrounded_cell_marker(self, board, r, c, visit):
        if r < 0 or c < 0 or c >= self.COLS or r >= self.ROWS or board[r][c] != "O" or (r, c) in visit:
            return
        board[r][c] = "T"
        visit.add((r,c))
        self.unsurrounded_cell_marker(board, r+1, c, visit)
        self.unsurrounded_cell_marker(board, r, c+1, visit)
        self.unsurrounded_cell_marker(board, r-1, c, visit)
        self.unsurrounded_cell_marker(board, r, c-1, visit)
        
''' Explanation 
Process
1. mark not-surrounded cells with new character - T 
2. visit all cells, and update O to X 
3. visit all cells, and update T to O 

과정:
1. DFS를 통해 'X'로 둘러쌓이지 않은 모든 셀을 'T'로 표시한다. 
2. 'O'를 'X'로 변경:모든 셀을 순회하면서 'O'를 'X'로 변경합니다. 
3. 마지막으로 'T'로 표시된 영역을 다시 'O'로 변경합니다.

T를 도입한 이유:
'T'는 둘러싸인 영역의 셀을 표시하기 위한 임시 마커.
이를 통해 'O'로 표시된 셀 중에서 실제로 'X'로 둘러싸인 영역에 속하는 것을 식별하고 변경할 수 있다. 
변경 후에는 'T'를 다시 'O'로 변경하여 영향을 받지 않는 영역을 보존함.
'''