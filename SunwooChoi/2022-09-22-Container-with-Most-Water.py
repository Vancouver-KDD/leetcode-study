class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = float('-inf')    
        
        while left < right:
            # calculate amount of water containing by current two poles
            cur_water = (right-left) * min(height[left], height[right])
            # update max
            max_water = max(max_water, cur_water)
            # we move smaller height to inner array
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_water