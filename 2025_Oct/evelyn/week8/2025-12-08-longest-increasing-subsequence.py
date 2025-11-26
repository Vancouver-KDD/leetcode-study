import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []

        for num in nums:
            idx = bisect.bisect_left(ans, num)
            
            if idx == len(ans):
                ans.append(num)
            else:
                ans[idx] = num

        return len(ans)