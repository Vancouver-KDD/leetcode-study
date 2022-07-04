/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    const dp = Array(amount+1).fill(Infinity);
    dp[0] = 0;
    
    for (var coin of coins) {
        for (var i=coin; i<=amount; i++){
            dp[i] = Math.min(dp[i], dp[i-coin]+1);
        }
    }
    
    return dp[amount] === Infinity ? -1 : dp[amount];
};
