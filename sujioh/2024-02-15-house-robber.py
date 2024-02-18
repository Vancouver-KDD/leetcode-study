# [2,7,9,3,1]
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dp[2] = max(nums[0]+nums[2], nums[1])
        for i in range(3, len(nums)): # 2 ~ 4 inclusive
            include_i = dp[i-2] + nums[i]
            exclude_i = dp[i-1]
            dp[i] = max(include_i, exclude_i)
        return dp[len(nums)-1]

nums = [6, 3, 10,  8,  2, 10, 3,  5,  10, 5, 3]
s = Solution()
s.rob(nums)

'''
이 문제는 주어진 어레이에서 가장 큰 "합"을 구하는 문제.
하지만 "인접한 수는 포함할 수 없다"는 조건이 있다. 

디피 어레이를 만든다.
디피 어레이는 그 인덱스까지의 가장 큰 합이다.
Using this DP array we can track the maximum sum until that index.

Example: 
the array we have is [6,3,10,8,2]
1. the dp[0] will store just arr[0], because it is the biggest number so far.add()
2. However, dp[1] will store the max number between arr[0] and arr[1]
3. dp[2] will store dp[0]+arr[2] OR dp[1] << and it is the core logic of this question. 
    - we can decided whether to include "arr[i]" or not. 

'''