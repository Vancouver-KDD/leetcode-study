class Solution:
    def rob(self, nums: List[int]) -> int:
        l, r = 0, 0
        for n in nums:
            temp = max(l + n, r)
            l = r
            r = temp
        return r