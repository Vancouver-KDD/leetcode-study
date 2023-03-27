class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[j][i] = 1 + dp[j+1][i+1]
                else:
                    dp[j][i] = max(dp[j][i+1], dp[j+1][i])
        
        return dp[0][0]
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        max_val, cur_sum = nums[0], 0
        for n in nums:
            if cur_sum < 0:
                cur_sum = n
            else:
                cur_sum += n
            max_val = max(max_val, cur_sum)
        return max_val
    
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= target:
                target = i
        return True if target == 0 else False      
    
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=(lambda x: x[0]))
        res = [intervals[0]]
        for inter in intervals[1:]:
            if res[-1][1] >= inter[0]:
                res[-1][1] = max(res[-1][1], inter[1])
            else:
                res.append(inter)
        return res
