function coinChange(coins, amount){
  dp = new Array(amount + 1).fill(Infinity);
  dp[0] = 0;

  for(let coin of coins) {
    for(let i = coin; i <= amount; i++){
      dp[i] = Math.min(dp[i], dp[i - coin]);
    }
  }
  return dp[amount] === Infinity ? -1 : dp[amount];
}