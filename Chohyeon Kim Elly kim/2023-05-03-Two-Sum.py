class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        for i in range (0, len(nums)):
            find = target - nums[i]

            for j in range (i+1, len(nums)):
                if find == nums[j]:
                    return [i,j]

        return [-1]