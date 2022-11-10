# 213. House Robber II

> Problem link: https://leetcode.com/problems/house-robber-ii/submissions/  
> submission detail: https://leetcode.com/submissions/detail/824112231/



```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
```