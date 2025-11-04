class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left, right = 0, len(height) -1
        # area: (right - left) * min(height[left], height[right])
        # update 'max_area'
        # height[left] < height[right] -> left += 1, otherwise right -= 1
        # iterate left < right

        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(curr_area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
