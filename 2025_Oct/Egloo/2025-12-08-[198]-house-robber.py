class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        def visit(place):

            if place == len(nums) - 1 or place == len(nums) - 2:
                return nums[place]
            elif place >= len(nums):
                return 0
            else:
                if place in cache:
                    return cache[place] 

                cache[place] = max(visit(place + 2), visit(place + 3)) + nums[place]
                return cache[place]

        return max(visit(0), visit(1))