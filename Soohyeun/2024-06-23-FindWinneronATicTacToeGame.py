class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        n = 3

        cols = [0] * n
        rows = [0] * n
        diag = 0
        anti_diag = 0
        count = 1 # A as 1, B as -1

        for index, move in enumerate(moves):
            row = move[0]
            col = move[1]
            # A moves
            rows[row] += count
            cols[col] += count
            if row == col:
                diag += count
            if row + col == n - 1:
                anti_diag += count
            if abs(rows[row]) == n or abs(cols[col]) == n or abs(diag) == n or abs(anti_diag) == n:
                return "A" if count == 1 else "B"
            count *= -1 # Update 'A to B' or 'B to A'

        return "Draw" if len(moves) == 9 else "Pending"