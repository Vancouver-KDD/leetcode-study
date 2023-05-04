# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #input nums = [2,7,11,15], target = 9
        #outpu [0,1]

        for i in range(len(nums)-1): #when i == 0
            for j in range(i+1, len(nums)): #start from 1 to 3
                if nums[i] + nums[j] == target :
                    return [i, j]
