class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
            
        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in hashMap:
                return [hashMap[remainder], index]
            hashMap[num] = index
            
        