// Write a function that takes an unsigned integer and
//Todo: returns the number of '1' bits it has.

//* Example 1:

// Input: n = 00000000000000000000000000001011
// Output: 3
// Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

//Todo: 0 & 0 => 0 / 0 & 1 => 0 / 1 & 1 => 1  모두 1이어야 1, 바뀐 1을 <<(shift to the left) 하면 carry value
//Todo: 0 | 0 => 0 / 0 | 1 => 1 / 1 | 1 => 1  1이 있기만 하면 1
//Todo: 0 ^ 0 => 0 / 0 ^ 1 => 1 / 1 ^ 1 => 0  1이 하나만 있어야 1, 더하기 연산과 비슷함

const hammingWeight = function (n) {
  let count = 0;
  while (n) {
    n = n & (n - 1);
    count++;
  }
  return count;
};

// Fail
// const hammingWeight = function (n) {
//   let count = 0;
//   while (n.length > 0) {
//     if (n % 2 !== 0) {
//       count++;
//       hammingWeight(n >> 1);
//     }
//   }
//   return count;
// };
