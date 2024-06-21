/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
function maximumSubarraySum(nums, k) {
  let maxSum = 0
  let curSum = 0
  let start = 0
  let same = new Map()

  for (let end = 0; end < nums.length; end++) {
    let endNum = nums[end]
    same.set(endNum, (same.get(endNum) || 0) + 1)
    curSum += endNum

    if (end >= k - 1) {
      if (same.size === k) {
        maxSum = Math.max(maxSum, curSum)
      }

      let startNum = nums[start]
      curSum -= startNum
      if (same.get(startNum) === 1) {
        same.delete(startNum)
      } else {
        same.set(startNum, same.get(startNum) - 1)
      }
      start++
    }
  }

  return maxSum
}

let nums = [1, 5, 4, 2, 9, 9, 9]
let k = 3
maximumSubarraySum(nums, k)
