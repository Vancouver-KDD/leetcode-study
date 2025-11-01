class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1

        area = 0
        while i < j:
            area = max((j-i) * min(height[i], height[j]), area)

            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return area