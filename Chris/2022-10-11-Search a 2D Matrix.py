class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low, high = 0, len(matrix)-1
    
        while True:
            mid = (low + high) // 2
                        
            if mid-low <= 1 and high-mid <= 1:
                if target >= matrix[high][0]:
                    row = high
                elif target >= matrix[mid][0]:
                    row = mid
                else:
                    row = low
                break
                    
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                low = mid
            else:
                high = mid
                
        
        
        l, r = 0, len(matrix[0])-1
        
        while l < r:
            m = (l + r)//2
            
            if target == matrix[row][m]:
                return True
            elif target < matrix[row][m]:
                r = m
            else:
                l = m+1
        
        return True if matrix[row][l] == target else False
            
            
        
        