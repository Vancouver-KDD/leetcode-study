from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx, num in enumerate(nums):
            if idx == 0 or (idx > 0 and nums[idx] <= 0 and nums[idx-1] != nums[idx]):
                left, right = idx + 1, len(nums) - 1
                while left < right:
                    three_sum = num + nums[left] + nums[right]
                    if three_sum > 0:
                        right -= 1
                    elif three_sum < 0:
                        left += 1
                    else:
                        res.append([num, nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left-1] and left < right:
                            left += 1
        return res