function numDecodings(s){
  const dp = new Array(s.length + 1).fill(0);

  dp[0] = 1;
  dp[1] = s.charAt(0) == '0' ? 0 : 1;

  for(let i = 2; i < s.length + 1; i++){
    // Get values for one and two digit numbers
    const lastOneDigit = s.slice(i-1, i);
    const lastTwoDigit = s.slice(i-2, i);

    // Check if one digit and/or two digit numbers are valid
    if(lastOneDigit > 0){
      dp[i] = dp[i-1];
    }
    if(lastTwoDigit >= 10 && lastTwoDigit <= 26){
      dp[i] = dp[i] + dp[i-2];
    }
  }
  return dp[s.length];
};