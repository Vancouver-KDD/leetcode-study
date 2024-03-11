from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for cur_target in range(1, target + 1):
            for num in nums:
                if cur_target - num >= 0:
                    dp[cur_target] += dp[cur_target - num]
                else:
                    break
        print(dp)
        return dp[target]


s = Solution()
nums = [1,2]
target = 10
s.combinationSum4(nums, target)

'''
1: 1 (1)
2: 2 (1,1) (2)
3: 3 (1,1,1) (2,1) (1,2)
4: 6 (1,1,1,1) (2,1,1) (1,2,1)
    (1,1,1,1) X (2,2)
    (1,1,1,1,1) X (1,2,1) (1,1,2)
5: 12


[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

'''






'''
3: 1
4: 1
5: 1
6: 2
7: 3
8: 1+1+1 +1 = 4
9: 3+2+1 = 6
10: 9
'''
