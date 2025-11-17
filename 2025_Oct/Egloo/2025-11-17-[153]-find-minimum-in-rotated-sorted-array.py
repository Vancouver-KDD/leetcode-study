class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        sv = nums[0]

        while i <= j:
            m = (i+j) // 2

            if nums[i] <= nums[m]:
                sv = min(sv, nums[i])
                i = m+1
            else:
                sv = min(sv, nums[m+1])
                j = m

        return sv