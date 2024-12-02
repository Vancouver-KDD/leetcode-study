class Solution {
  /**
   * @param {number[]} nums
   * @return {number}
   */
  lengthOfLIS(nums) {
    return this.dfs(nums, 0, -1);
  }

  /**
   * @param {number[]} nums
   * @param {number} i
   * @param {number} j
   * @return {number}
   */
  dfs(nums, i, j) {
    if (i === nums.length) {
      return 0;
    }

    let LIS = this.dfs(nums, i + 1, j); // not include

    if (j === -1 || nums[j] < nums[i]) {
      LIS = Math.max(LIS, 1 + this.dfs(nums, i + 1, i)); // include
    }

    return LIS;
  }
}
