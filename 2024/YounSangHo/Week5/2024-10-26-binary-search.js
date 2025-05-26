class Solution {
  /**
   * @param {number[]} nums
   * @param {number} target
   * @return {number}
   */
  search(nums, target) {
    let start = 0;
    let end = nums.length - 1;

    while (start <= end) {
      let mid = parseInt((start + end) / 2);

      console.log(mid);
      if (nums[mid] === target) {
        return mid;
      } else if (nums[mid] > target) {
        end = mid - 1;
      } else if (nums[mid] < target) {
        start = mid + 1;
      }

      console.log(`start : ${start}`);
      console.log(`end : ${end}`);
    }

    return -1;
  }
}
