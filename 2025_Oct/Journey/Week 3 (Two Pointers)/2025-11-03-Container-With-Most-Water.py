class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Start with two pointers:
        # 'l' (left) at the beginning and 'r' (right) at the end of the array
        l = 0
        r = len(height) - 1

        # This variable will store the maximum amount of water found so far
        max_water = 0

        # Continue while the two pointers haven't met
        while l < r:
            # Find the current area:
            # height is limited by the shorter line (min(height[l], height[r]))
            # width is the distance between the two lines (r - l)
            curr = min(height[l], height[r]) * (r - l)

            # Update the maximum area if the current one is bigger
            max_water = max(max_water, curr)

            # Move the pointer that has the shorter line:
            # because the taller one cannot increase the area
            if height[l] < height[r]:
                l += 1 # Move left pointer to the right
            else:
                r -= 1 # Move right pointer to the left

        # Return the largest area found
        return max_water