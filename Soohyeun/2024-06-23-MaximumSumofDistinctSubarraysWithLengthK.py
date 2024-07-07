class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr_window = {}
        curr_sum = 0
        max_sum = 0
        left = 0

        for right, num in enumerate(nums):
            curr_window[num] = curr_window.get(num, 0) + 1
            curr_sum += num
            if right - left + 1 == k:
                if len(curr_window) == k:
                    max_sum = max(max_sum, curr_sum)
                curr_window[nums[left]] -= 1
                if curr_window[nums[left]] == 0:
                    del curr_window[nums[left]]
                curr_sum -= nums[left]
                left += 1
        return max_sum
