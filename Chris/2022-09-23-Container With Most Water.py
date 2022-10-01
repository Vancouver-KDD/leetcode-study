class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxArea = 0
        l , r = 0 , len(height)-1
        
        while l < r:
            
            cur = min(height[l], height[r]) * (r - l)
            
            if cur > maxArea:
                maxArea = cur
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return maxArea
            
            