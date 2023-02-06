class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            m = i + (j - i) // 2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
        return nums[i]

# time = log n
# spcae = 1