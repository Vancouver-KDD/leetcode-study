class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = -1
        first = 0
        end = len(nums) - 1
        while first <= end:
            mid = first + (end - first)/2
            if nums[mid] == target:
                index = mid
                break;
            elif nums[mid] < target:
                first = mid + 1
            elif nums[mid] > target:
                end = mid - 1

        return index