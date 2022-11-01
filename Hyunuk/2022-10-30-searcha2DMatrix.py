class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        l = 0
        r = row * col
        while l < r:
            m = (l + r) // 2
            m_r, m_c = divmod(m, col)
            curr = matrix[m_r][m_c]
            if curr == target:
                return True
            elif curr < target:
                l = m + 1
            else:
                r = m
        return False
