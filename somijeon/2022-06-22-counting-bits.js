// Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
//Todo: ans[i] is the number of 1's in the binary representation of i.

//* Example 1:

// Input: n = 5
// Output: [0,1,1,2,1,2]
// Explanation:
// 0 --> 0
// 1 --> 1
// 2 --> 10
// 3 --> 11
// 4 --> 100
// 5 --> 101

const countBits = function (n) {
  let res = [0];
  for (let i = 1; i <= n; i++) {
    const half = i >> 1;
    const odd = i & 1;
    res[i] = res[half] + odd;
  }
  return res;
};

// Fail
// const countBits = function (n) {
//   const hammingWeight = function (n) {
//     let count = 0;
//     while (n) {
//       n = n & (n - 1);
//       count++;
//     }
//     return count;
//   };

//   let answer = [];
//   for (let i = 0; i <= n; i++) {
//     answer.push(hammingWeight(i.toString(2)));
//   }
//   return answer;
// };
