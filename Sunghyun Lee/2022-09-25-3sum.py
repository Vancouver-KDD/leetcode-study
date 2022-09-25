class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = [];
        nums.sort();
        for i , f in enumerate(nums):
            if i > 0 and f == nums[i-1]:
                continue;
            l = i+1
            r = len(nums)-1;
            while l < r:
                if f + nums[l] + nums[r] == 0:
                    result.append([f,nums[l] ,nums[r]]);
                    l += 1;
                    while l< r and nums[l]== nums[l-1]:
                            l += 1;
                elif f + nums[l] + nums[r] < 0:
                    l+=1;
                elif f + nums[l] + nums[r]> 0:
                    r -=1;
        return result;
