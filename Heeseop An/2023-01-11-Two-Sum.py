class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in dic:
                return [i, dic[remaining]]
            dic[nums[i]] = i
        

        # #brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if target - nums[j] == nums[i]:
        #             return [i, j]
            
        
