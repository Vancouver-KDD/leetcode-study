# 198. House Robber

> Problem link: https://leetcode.com/problems/house-robber/  
> submission detail: https://leetcode.com/submissions/detail/822682958/

```py
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # i번째 집은 도둑질 할때 최대값은 아래 두가지의 최대값이다
        # i-2번째 집까지의 도둑질양 + 현재 i번째집 도둑질 양
        # i-1번째 집까지의 도둑질양
        nums[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])

        return nums[len(nums) - 1]
```
