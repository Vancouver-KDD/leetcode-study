class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        while left < right and top < bottom:
            # add top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # add right most column
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            # overlap condition check
            if not (left < right and top < bottom):
                break
            # add bottom row
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
            # add left most column
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
