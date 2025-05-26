class Solution {
  /**
   * @param {number[]} cost
   * @return {number}
   */
  minCostClimbingStairs(cost) {
    const dfs = (i) => {
      if (i >= cost.length) {
        return 0;
      }
      return cost[i] + Math.min(dfs(i + 1), dfs(i + 2));
    };
    return Math.min(dfs(0), dfs(1));
  }
}
