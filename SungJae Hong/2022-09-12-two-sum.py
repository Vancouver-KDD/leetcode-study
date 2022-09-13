class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """My original answer"""
        # list_size = len(nums)
        # newlist = []
        # for x in range(0, list_size):
        #     for y in range(x+1,list_size):
        #         if nums[x] + nums[y] == target:
        #             newlist.append(x)
        #             newlist.append(y)
        #             return newlist

        #Initialize empty hashmap
        hashmap = {}

        #Fill up the hashap using the enumerate fuction.
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
