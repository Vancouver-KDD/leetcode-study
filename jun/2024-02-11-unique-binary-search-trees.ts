// stp 1: recursion
function numTrees(n: number): number {
  if (n < 2) {
    return 1
  }
  let result = 0
  for (let root = 1; root <= n; root++) {
    result += numTrees(root - 1) * numTrees(n - root)
  }
  return result
}

// solution: Applied Dynamic programming
function numTrees(n: number): number {
  const dp = [1, 1]

  for (let root = 2; root <= n; root++) {
    dp[root] = 0
    for (let i = 1; i <= root; i++) {
      dp[root] += dp[i - 1] * dp[root - i]
    }
  }
  return dp[n]
}
