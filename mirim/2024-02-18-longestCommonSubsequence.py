# https://leetcode.com/problems/longest-common-subsequence/description/
# dp bottom up solution. time, complex = O(n*m)
def longestCommonSubsequence(text1: str, text2: str) -> int:
    # dp = [[0] * len(text2) for _ in range(text1)]
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

    return dp[0][0]


print(longestCommonSubsequence("abcde", "ace"))
