function longestCommonSubsequence(text1: string, text2: string): number {
  const dp: number[][] = Array.from({ length: text1.length + 1 }, () =>
    Array(text2.length + 1).fill(0)
  )

  for (let i = text1.length - 1; i >= 0; i--) {
    for (let j = text2.length - 1; j >= 0; j--) {
      dp[i][j] =
        text1[i] === text2[j]
          ? dp[i + 1][j + 1] + 1
          : 0 + Math.max(dp[i + 1][j], dp[i][j + 1])
    }
  }
  return dp[0][0]
}
