class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        result = set()
        for num in nums:
            if num not in result:
                result.add(num)
            else:
                return True
        return False
