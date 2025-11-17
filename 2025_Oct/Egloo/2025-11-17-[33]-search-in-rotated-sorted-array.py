class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j = 0, len(nums) - 1

        while i <= j:
            m = (i+j) // 2
            if nums[m] == target:
                return m
            if nums[i] <= nums[m]:
                if target >= nums[i] and target <= nums[m]:
                    return self.binarySearch(nums, i, m, target)
                else:
                    i = m + 1
            else:
                if target >= nums[m+1] and target <= nums[j]:
                    return self.binarySearch(nums, m+1, j, target)
                else:
                    j = m-1
        return -1

    def binarySearch(self, nums, i, j, target):
        while i <= j:
            m = (i+j)//2

            if nums[m] == target:
                return m
            elif target < nums[m]:
                j = m - 1
            else:
                i = m + 1
        return -1