from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_idx, r_idx = 0, len(height) - 1
        res = 0
        while l_idx < r_idx:
            bucket_height = min(height[l_idx],height[r_idx])
            area = (r_idx - l_idx) * bucket_height
            res = max(res, area)
            
            if height[l_idx] < height[r_idx]:
                l_idx += 1
            else:
                r_idx -= 1
        return res
    