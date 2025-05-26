class Solution {
  /**
   * @param {number[]} nums
   * @return {number}
   */
  rob(nums) {
    // 1. nums[i] is the amount of money the i th house has.
    // 2. the houses are arranged in a circle
    // 3. can't rob two adjacent houses
    return Math.max(
      nums[0],
      Math.max(this.helper(nums.slice(1)), this.helper(nums.slice(0, -1)))
    );
  }

  /**
   * @param {number[]} nums
   * @return {number}
   */
  helper(nums) {
    let rob1 = 0;
    let rob2 = 0;
    for (const num of nums) {
      const newRob = Math.max(rob1 + num, rob2);
      rob1 = rob2;
      rob2 = newRob;
    }
    return rob2;
  }
}
