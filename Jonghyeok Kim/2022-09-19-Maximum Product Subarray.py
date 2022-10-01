class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p, min_p, cur_p = max(nums), 1, 1
        for n in nums:
            tmp = cur_p * n
            cur_p = max(cur_p * n, min_p *n, n)
            min_p = min(tmp, min_p * n, n)
            max_p = max(max_p, cur_p)
        return max_p
