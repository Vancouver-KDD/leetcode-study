class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height)-1
        maxArea = 0
        while l<r:
            area = (r-l) * min(height[l], height[r])
            maxArea = max(area, maxArea)
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea
