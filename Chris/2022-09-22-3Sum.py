class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        
        length = len(nums)
        
        res = []
        for i, num in enumerate(nums[:-2]):
            
            if num > 0:
                break
                
            if i > 0 and nums[i-1] == num:
                continue
            
            target = -num
            
            l , r = i+1, length-1
            
            while l < r:
                if  l != i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
            
                if nums[l] + nums[r] == target:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        
        return res
            