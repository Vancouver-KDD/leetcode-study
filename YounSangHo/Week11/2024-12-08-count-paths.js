class Solution {
  /**
   * @param {number} m
   * @param {number} n
   * @return {number}
   */
  uniquePaths(m, n) {
    const memo = Array.from({ length: m }, () => Array(n).fill(-1));
    const dfs = (i, j) => {
      if (i == m - 1 && j == n - 1) {
        return 1;
      }
      if (i >= m || j >= n) return 0;
      if (memo[i][j] != -1) {
        return memo[i][j];
      }
      memo[i][j] = dfs(i, j + 1) + dfs(i + 1, j);
      return memo[i][j];
    };

    return dfs(0, 0);
  }
}
