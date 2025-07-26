class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        path=[]
        result=[]

        def backtracking(path,nums,index):
            print(path)
            result.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtracking(path,nums,i+1)
                path.pop()
        backtracking(path, nums, 0)

        return result
