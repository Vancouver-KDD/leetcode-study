class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        # idx -> 0 to n - 1
        # val -> distinct number in [0, n]
        for idx, val in enumerate(nums):
            ans ^= idx
            ans ^= val
        return ans
