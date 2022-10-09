// 모르겠다
var coinChange = function(coins, amount) {
  var dp = [];
  return coin(coins, amount, dp);
};

var coin = function (coins, amount, dp) {
  if (dp[amount - 1] !== undefined) return dp[amount - 1];
  if (amount < 0) return -1;
  if (amount === 0) return 0;

  var count = Number.MAX_SAFE_INTEGER;
  var tmp = 0;

  for (var i = 0; i < coins.length; i++) {
    tmp = coin(coins, amount - coins[i], dp);
    if (tmp !== -1) count = Math.min(count, tmp + 1);
  }

  dp[amount - 1] = count === Number.MAX_SAFE_INTEGER ? -1 : count;

  return dp[amount - 1];
};
