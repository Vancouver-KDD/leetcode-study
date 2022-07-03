var wordBreak = function (s, wordDict) {
  let dp = new Array(s.length + 1).fill(false);
  dp[0] = true;

  for(let i = 0; i <= s.length; i++){
    if(dp[i] === true){
      for(let word of wordDict){
        if(s.slice(i, i + word.length) === word){
          dp[i + word.length] = true;
        }
      }
    }
  }
  return dp[s.length];
};