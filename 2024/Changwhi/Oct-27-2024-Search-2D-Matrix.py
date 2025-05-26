class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        ROW, COL = len(matrix), len(matrix[0])
        
        top, bot = 0, ROW - 1
        while top <= bot:
            mid = (top + bot) // 2
            if target < matrix[mid][0]:
                bot = bot - 1
            elif target > matrix[mid][-1]:
                top = top + 1
            else: 
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        left, right = 0, COL -1
        
        while left <= right:
            mid = (left + right) //2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid -1
            else:
                return True
        return False
        
        