class Solution {
  /**
   * @param {number[]} nums
   * @return {number}
   */
  rob(nums) {
    // nums[i] the amount of money the 'i'th house has
    // the house are arranged in a straight
    // i can't rob two adjacent houses
    // my goal is maximum amount of money i can rob without alerting

    let rob1 = 0;
    let rob2 = 0;

    for (const num of nums) {
      const temp = Math.max(num + rob1, rob2);
      rob1 = rob2;
      rob2 = temp;
    }
    return rob2;
  }
}
