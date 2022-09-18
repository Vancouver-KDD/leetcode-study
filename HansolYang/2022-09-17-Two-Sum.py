class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {nums[i]:i for i in range(len(nums))}
        
        for i in range(len(nums)):
            toFind = target - nums[i]
            if (hashMap.get(toFind, False)) and hashMap.get(toFind) != i:
                return [i, hashMap.get(toFind)]