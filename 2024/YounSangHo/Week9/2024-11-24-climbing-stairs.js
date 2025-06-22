class Solution {
  /**
   * @param {number} n
   * @return {number}
   */
  climbStairs(n) {
    // 피보나치 수열
    // 1 1 2 3 5
    let preValue = 0;
    let curValue = 1;
    let result = 0;
    for (let i = 0; i < n; i++) {
      result = preValue + curValue;
      preValue = curValue;
      curValue = result;
    }

    return result;
  }
}
