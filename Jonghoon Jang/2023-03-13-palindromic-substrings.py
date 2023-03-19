"""
70. Climbing Stairs
"""

class Solution:
    # bottom-up approach
    # O(n^2)
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # 2D boolean array dp[i][j]
        # True: Palindrome
        # dp[i][j] i True if dp[i+1][j-1] true and s[i] == s[j]
        # aaaa  =>    dp[1][2]: True s[0] == s[3]  => Palindrome

        dp = [[False] * n for _ in range(n)]
        count = 0

        # base cases
        # substring has len 1 => always palindrome
        # subs has len 2 => palindrome if s[i] == s[i+1]
        for i in range(n):
            dp[i][i] = True
            count += 1
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                count += 1

        # fill dp array
        # substring >= 3
        # O(n^2)
        for k in range(3, n + 1):  # all possible len >= 3
            for i in range(n - k + 1):
                # s[i ... j] with len k
                j = i + k - 1
                # i: start char, j: end char
                if s[i] == s[j] and dp[i + 1][j - 1]:  # check palindrome O(1) using dp
                    dp[i][j] = True
                    count += 1
        return count


def main():
    s = Solution()


if __name__ == "__main__":
    main()
