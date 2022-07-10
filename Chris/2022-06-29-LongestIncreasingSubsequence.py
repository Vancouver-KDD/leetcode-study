# O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = [1] * len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if(nums[i] < nums[j]):
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        return max(LIS)



#O(nlogn)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        
        
        for num in nums:
            l, r = 0, size
            while(l < r):
                m = (l+r)//2
                if(num > tails[m]):
                    l = m + 1
                else:
                    r = m
            
            tails[l] = num
            size = max(size , l +1)
        
        return size