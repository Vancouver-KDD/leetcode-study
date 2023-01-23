"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    # Double pointers
    # Time complexity: O(n): single pass
    # Space complexity: O(1)
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            h = min(height[l], height[r])
            s = r - l
            current_area = h * s
            max_area = max(max_area, current_area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area


def main():
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    print(s.maxArea())


if __name__ == "__main__":
    main()
