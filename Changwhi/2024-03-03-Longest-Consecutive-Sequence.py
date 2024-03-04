class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        this is wrong solution since sort() method in python runs in O(n log n) time.
        """
#         if not len(nums):
#             return 0
#         res1 = 1
#         res2= 1
#         nums.sort()
        
#         for index in range(len(nums)-1):
#             if nums[index] + 1 == nums[index+1]:
#                 res1 += 1
#             elif nums[index] != nums[index+1]:
#                 res1=1
          
#             res2 = max(res1, res2)
#         return res2
        """
        Instead, I need to use set to retrieve elements from a given list in O(n) time
        
        """
        setNums = set(nums)
        res = 0
        
        for num in setNums:
            if (num - 1) not in setNums:
                length = 1
                while (num + length) in setNums:
                    length += 1
                res = max(length, res)
        return res
