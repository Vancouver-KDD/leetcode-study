class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return min(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            prev = (m-1) % len(nums)
            next_ = (m+1) % len(nums)
            if nums[prev] > nums[m] < nums[next_]:
                return nums[m]
            if nums[m] > nums[next_]:
                return nums[next_]
            
            if nums[m] > nums[0]:
                l = m + 1
            else:
                r = m - 1
