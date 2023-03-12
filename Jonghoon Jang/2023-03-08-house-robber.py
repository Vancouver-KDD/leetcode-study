"""
70. Climbing Stairs
"""

class Solution:

    def rob(self, nums) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # A, B, C
            #       ^
            # two ways: A + C  vs  B
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]



def main():
    s = Solution()


if __name__ == "__main__":
    main()
