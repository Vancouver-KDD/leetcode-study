class Solution(object):
    def twoSum(self, nums, target):

        # val : index
        dic = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dic:
                return[dic[diff] , i]
            else:
                dic[n] =i