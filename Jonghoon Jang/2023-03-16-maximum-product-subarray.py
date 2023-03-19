"""
70. Climbing Stairs
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min = 1
        curr_max = 1

        for num in nums:
            temp = curr_max * num
            curr_max = max(curr_max * num, curr_min * num, num)  # [-1, 8] itself
            curr_min = min(temp, curr_min * num, num)
            res = max(res, curr_max)
        return res
def main():
    s = Solution()


if __name__ == "__main__":
    main()
