class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        path = []

        def dfs():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in nums:
                if num not in path:
                    path.append(num)
                    dfs()
                    path.pop()

        dfs()
        return result
