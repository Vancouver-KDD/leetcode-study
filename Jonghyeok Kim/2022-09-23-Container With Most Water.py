class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, res = 0, len(height) - 1, 0
        while (left < right):
            # width * height where height is min btw right and left
            width = right-left
            # move the smaller pointer of height
            if height[right] > height[left]:
                res = max(res, width*height[left])
                left += 1
            else:
                res = max(res, width*height[right])
                right -= 1
        return res