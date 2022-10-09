class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_so_far = height[l]
        right_so_far = height[r]
        ret = 0
        while l < r:
            left_so_far = max(left_so_far, height[l])
            right_so_far = max(right_so_far, height[r])
            if left_so_far < right_so_far:
                ret += min(right_so_far, left_so_far) - height[l]
                l += 1
            else:
                ret += min(right_so_far, left_so_far) - height[r]
                r -= 1
        return ret
