class Solution {
  constructor() {
    this.res = [];
  }

  /**
   * @param {number[]} candidates
   * @param {number} target
   * @return {number[][]}
   */
  combinationSum2(candidates, target) {
    this.res = [];
    candidates.sort((a, b) => a - b);
    this.dfs(candidates, target, 0, [], 0);
    return this.res;
  }

  /**
   * @param {number[]} candidates
   * @param {number} target
   * @param {number} i
   * @param {number[]} cur
   * @param {number} total
   * @return {void}
   */
  dfs(candidates, target, i, cur, total) {
    if (total === target) {
      this.res.push([...cur]);
      return;
    }
    if (total > target || i === candidates.length) {
      return;
    }

    cur.push(candidates[i]);
    this.dfs(candidates, target, i + 1, cur, total + candidates[i]);
    cur.pop();

    while (i + 1 < candidates.length && candidates[i] === candidates[i + 1]) {
      i++;
    }
    this.dfs(candidates, target, i + 1, cur, total);
  }
}
