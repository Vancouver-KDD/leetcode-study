class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target: # 0 1 2 3| 4 5 6 7 target:6
                left = mid + 1
            elif nums[mid] > target: # 0 1 2 3| 4 5 6 7 target:2
                right = mid -1
        return -1
