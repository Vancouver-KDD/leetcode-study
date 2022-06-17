class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [2,3,-2,4] -> 2 * 3 : should be consecutive subarray
        # commit test1 2 3 4

        find = max(nums)
        curMaxpro, curMinpro = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMaxpro * n
            curMaxpro = max(n * curMaxpro, n * curMinpro, n)
            curMinpro = min(tmp, n * curMinpro, n)
            find = max(find, curMaxpro)
        return find