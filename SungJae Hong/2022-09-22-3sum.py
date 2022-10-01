from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Empty list to store results
        res = []
        # First sort the array in order to avoid duplicate list.
        nums.sort()
        # First for loop to store the first value out of 3.
        for i, a in enumerate(nums):
            #Checking to see if value next to each other is same value
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
