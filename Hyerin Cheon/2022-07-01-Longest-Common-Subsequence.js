var longestCommonSubsequence = function (text1, text2){
  const dp = [];

  for(let i = 0; i < text1.length + 1; i++){
    dp[i] = new Array(text2.length + 1).fill(0);
  }

  for(let i = 1; i <= text1.length; i++){
    for(let j = 1; j <= text2.length; j++){
      if(text1.charAt(i - 1) != text2.charAt(j - 1)){
        dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
      }else {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      }
    }
  }
  return dp[text1.length][text2.length];
}