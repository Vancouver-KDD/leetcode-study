class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while l < len(nums) - 1:
            if nums[l] + nums[r] == target:
                return [l, r]
            elif r >= len(nums) - 1:
                l += 1
                r = l + 1
            else:
                r += 1
                
        return []
        