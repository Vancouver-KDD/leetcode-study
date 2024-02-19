function wordBreak(s: string, wordDict: string[]): boolean {
  const dp = new Array(s.length + 1)
  dp[0] = true
  for (let subLeng = 1; subLeng <= s.length; subLeng++) {
    for (let i = 0; i < subLeng; i++) {
      dp[subLeng] = dp[i] && wordDict.includes(s.substring(i, subLeng))
      if (dp[subLeng]) {
        break
      }
    }
  }
  return dp[s.length]
}
