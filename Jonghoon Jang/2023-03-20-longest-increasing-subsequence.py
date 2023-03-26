"""
70. Climbing Stairs
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            # i = bisect_left(sub, num)
            lo, hi = 0, None
            while lo < hi:
                mid = (lo + hi) // 2
                if sub[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            i = lo

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)

            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num

        return len(sub)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
