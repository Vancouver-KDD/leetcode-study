from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


solution = Solution()
output = solution.searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)
print(output)
