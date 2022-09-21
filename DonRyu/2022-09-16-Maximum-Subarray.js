// Example 1:
// Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
// Output: 6
// Explanation: [4,-1,2,1] has the largest sum = 6.
// Example 2:

// Input: nums = [1]
// Output: 1
// Example 3:

// Input: nums = [5,4,-1,7,8]
// Output: 23
//
// let maxSubArray0 = (nums) => {
//   if (nums.length === 1) return nums[0]
//   let maxSum = 0
//   let prefix = 0
//
//   for (let a = 0; a < nums.length; a++) {
//     prefix = nums[a] + nums[a + 1]
//     if (prefix > 0) {
//       maxSum = prefix
//     } else {
//       prefix = 0
//     }
//   }
//   return maxSum
// }

let maxSubArray = (nums) => {
  if (nums.length === 1) return nums[0]

  let maxValue = nums[0]
  let accNum = nums[0]

  for (let i = 1; i < nums.length; i++) {
    let calc = Math.max(nums[i], accNum + nums[i])
    if(calc >maxValue ) {
        maxValue = calc
    }
    accNum = calc
  }
  return maxValue

}


// let maxSubArray = function (nums) {
//   let maxSum = nums[0];
//
//   for (let a = 1; a < nums.length; a++) {
//     nums[a] = Math.max(nums[a], nums[a] + nums[a - 1])
//     maxSum = Math.max(nums[a], maxSum)
//   }
//   return maxSum
// };


console.log(answerSub([-2,-1]))

