class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # These two blocks of code just target the time complexity in this
        # specific questions not for real backtracking algorithm.
        ##################################################################
        # count = Counter(sum(board, []))
        # for c, countWord in Counter(word).items():
        #     if count[c] < countWord:
        #         return False

        # if count[word[0]] > count[word[-1]]:
        #     word = word[::-1]
        ##################################################################
        
        def helper(row, col, idx, tracking):
            res = False
            if (row, col) not in tracking:
                tracking.add((row, col))
                if idx < len(word) and board[col][row] == word[idx]:
                    if idx == len(word)-1:
                        return True
                    if row > 0 and (row-1, col) not in tracking:
                        res = res or helper(row-1, col, idx+1, tracking.copy())
                    if col > 0 and (row, col-1) not in tracking:
                        res = res or helper(row, col-1, idx+1, tracking.copy())
                    if row < len(board[0])-1 and (row+1, col) not in tracking:
                        res = res or helper(row+1, col, idx+1, tracking.copy())
                    if col < len(board)-1 and (row, col+1) not in tracking:
                        res = res or helper(row, col+1, idx+1, tracking.copy())
                    return res
            return False
        
        for col in range(len(board)):
            for row in range(len(board[0])):
                if helper(row, col, 0, set()):
                    return True
        
        return False
                