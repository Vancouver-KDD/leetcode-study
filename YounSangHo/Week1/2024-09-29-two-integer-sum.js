class Solution {
  /**
   * @param {number[]} nums
   * @param {number} target
   * @return {number[]}
   */
  twoSum(nums, target) {
    let checkMap = new Map();
    let resultArr = [];

    nums.forEach((num, index) => {
      let otherVal = target - num;
      if (!checkMap.has(otherVal)) {
        checkMap.set(num, index);
      } else {
        resultArr = [index, checkMap.get(otherVal)];
      }
    });

    return resultArr;
  }
}
