class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ret = 0
        while l < r:
            w = r - l
            if height[l] < height[r]:
                ret = max(ret, w * height[l])
                l += 1
            else:
                ret = max(ret, w * height[r])
                r -= 1
        return ret
