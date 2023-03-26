"""
70. Climbing Stairs
"""

class Solution:
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        memo = [0] * len(nums)
        memo[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            memo[i] = max(nums[i], memo[i-1] + nums[i])
            max_sum = max(max_sum, memo[i])

        return max_sum



def main():
    s = Solution()


if __name__ == "__main__":
    main()
