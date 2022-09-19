class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        for k, v in cnt.items():
            if v == 1:
                return k
