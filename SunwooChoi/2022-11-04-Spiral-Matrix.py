class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])-1
        top, bot = 0, len(matrix)-1
        
        ans = []
        
        while left <= right and top <= bot:
            # traverse from top-left to top-right
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top += 1
            # traverse from top-right to right-bottom
            for i in range(top, bot+1):
                ans.append(matrix[i][right])
            right -= 1
            # traverse from right-bottom to left-bottom
            if top <= bot:
                for i in range(right, left-1,-1):
                    ans.append(matrix[bot][i])
                bot -= 1
            # traverse from left-bottom to left-top    
            if left <= right:
                for i in range(bot, top-1, -1):
                    ans.append(matrix[i][left])
                left += 1
            
        return ans
    
