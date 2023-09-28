class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexMap = {}

        for i in range(len(nums)):
            potentialMatch = target - nums[i]
            if potentialMatch in indexMap:
                return [i, indexMap[potentialMatch]]
            indexMap[nums[i]] = i
