class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums, 0, result)
        return result

    def helper(self, nums, idx, result):
        if len(nums) == idx:
            result.append(list(nums))
            return
        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx] , nums[i]
            self.helper(nums, idx+1, result)
            nums[i], nums[idx] = nums[idx] , nums[i]


s = Solution()
r = s.permute([1,2,3])
print(r)
