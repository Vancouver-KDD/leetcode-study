# You are given an integer array nums and and integer k
# Find the maximum subarray sum of all the subarray of nums that meet the following conditions
# The length of the subarray is k
# All the elements of the subarray are distinct
# A subarray contiguous non empty suquence of element within array

# [1, 5, 4, 2, 9, 9, 9], k = 3
# return 15

class Soltuion:
    def maxSumSubarrayK(self, nums, k):
        l = 0
        maxSum = 0
        currSum = 0
        currSet = set()
        for r, num in enumerate(nums):
            while num in currSet:
                currSum -= nums[l]
                currSet.remove(nums[l])
                l += 1

            currSum += num
            currSet.add(num)
            length = r - l + 1

            if length == k:
                maxSum = max(maxSum, currSum)
                currSet.remove(nums[l])
                currSum -= nums[l]
                l += 1

        return [k, maxSum]
