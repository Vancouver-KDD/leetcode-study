class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        bs = [False for _ in range(len(nums))]
        self.sub(nums, bs, 0, result) 
        return result

    def sub(self, nums, bs, idx, result):
        if idx == len(nums):
            r = []
            for i, b in enumerate(bs):
                if b:
                    r.append(nums[i])
            result.append(r)
            return 

        bs[idx] = True 
        self.sub(nums, bs, idx+1, result)
        bs[idx] = False
        self.sub(nums, bs, idx+1, result)