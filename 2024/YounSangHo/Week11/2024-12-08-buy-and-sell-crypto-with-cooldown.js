class Solution {
  /**
   * @param {number[]} prices
   * @return {number}
   */
  maxProfit(prices) {
    const dp = {};
    const dfs = (i, buying) => {
      if (i >= prices.length) {
        return 0;
      }
      let key = `${i}-${buying}`;
      if (key in dp) {
        return dp[key];
      }

      let cooldown = dfs(i + 1, buying);
      if (buying) {
        let buy = dfs(i + 1, false) - prices[i];
        dp[key] = Math.max(buy, cooldown);
      } else {
        let sell = dfs(i + 2, true) + prices[i];
        dp[key] = Math.max(sell, cooldown);
      }
      return dp[key];
    };

    return dfs(0, true);
  }
}
