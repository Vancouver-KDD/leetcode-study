# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Input: height = [1,1]
# Output: 1


class Solution:
    # Solution 1: Brute Force - Two pointers
    def maxArea(self, height: list[int]) -> int:
        current_x = []
        current_y = []
        max_area = 0

        for i in range(len(height)):
            for j in range(i+1, len(height)):
                current_y.append(min(height[i], height[j]))
                current_x.append(j - i)

        print("x: ", str(current_x))
        print("y: ", str(current_y))

        for i in range(len(current_x)):
            if max_area < (current_x[i] * current_y[i]):
                max_area = current_x[i] * current_y[i]

        return max_area

    # Solution 2:
    def maxArea_2(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            max_area = max(max_area, min(height[left], height[right]) * width)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
