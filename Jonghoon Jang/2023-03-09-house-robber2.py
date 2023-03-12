"""
70. Climbing Stairs
"""

class Solution:

    def rob(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # Rob the first house, but not the last house
        dp1 = [0] * (n-1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])

        # Rob the last house, but not the first house
        dp2 = [0] * (n-1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])
        for i in range(2, n-1):
            dp2[i] = max(dp2[i-2] + nums[i+1], dp2[i-1])

        return max(dp1[-1], dp2[-1])



def main():
    s = Solution()


if __name__ == "__main__":
    main()
