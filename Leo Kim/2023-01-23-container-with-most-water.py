class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        mostWater = 0

        while left <= right:
            hori = (right - left)
            vert = min(height[right], height[left])
            mostWater = max(mostWater, hori * vert)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return mostWater
        # TC: O(n) SC: O(1)