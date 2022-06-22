class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = right * min(height[left], height[right])
        while (left < right):
            if (height[left] < height[right]):
                left+=1
            else:
                right-=1
            maxarea = max(maxarea, min(height[left], height[right]) * (right - left))
        return maxarea
