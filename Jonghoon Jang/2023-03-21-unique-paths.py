"""
70. Climbing Stairs
"""
from enum import Enum

class Index(Enum):
    GOOD = 1
    BAD = 2
    UNKNOWN = 3


class Solution:
    def canJump(self, nums) -> bool:
        memo = [Index.UNKNOWN] * len(nums)
        memo[-1] = Index.GOOD

        for i in range(len(nums) - 2, -1, -1):
            furthest_jump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthest_jump + 1):
                if memo[j] == Index.GOOD:
                    memo[i] = Index.GOOD
                    break

        return memo[0] == Index.GOOD


def main():
    s = Solution()


if __name__ == "__main__":
    main()
