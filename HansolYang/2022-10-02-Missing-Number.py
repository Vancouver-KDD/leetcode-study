class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor = 0
        for i in nums:
            xor = xor ^ i
            print(xor)
 
        for i in range(len(nums) + 1):
            xor = xor ^ i
            print(xor)
 
        return xor