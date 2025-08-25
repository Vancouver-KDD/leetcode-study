# Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = []

        for i in range(n):
            curr = nums[i]
            if not sub or curr > sub[-1]:
                sub.append(curr)
            else:
                sub[bisect.bisect_left(sub, curr)] = curr
        return len(sub)