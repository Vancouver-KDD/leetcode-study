class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        ans = nums[0]
        cur_max, cur_min = nums[0],nums[0]
        
        # since the type of list is integer, there is no possibility to decrease abs value
        for i in range(1, len(nums)):
            # if cur_max and cur_min == 0, then start subarray from i
            cur_max_tmp = max(cur_max*nums[i], cur_min*nums[i], nums[i])
            cur_min_tmp = min(cur_max*nums[i], cur_min*nums[i], nums[i])
            cur_max = cur_max_tmp
            cur_min = cur_min_tmp
            # update answer
            ans = max(cur_max, ans)
        return ans
            