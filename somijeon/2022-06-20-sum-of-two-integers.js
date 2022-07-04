// Given two integers a and b, return the sum of the two integers
//* without using the operators + and -.

//* Example 1:

// Input: a = 1, b = 2
// Output: 3

//Todo: 0 & 0 => 0 / 0 & 1 => 0 / 1 & 1 => 1  모두 1이어야 1, 바뀐 1을 <<(shift to the left) 하면 carry value
//Todo: 0 | 0 => 0 / 0 | 1 => 1 / 1 | 1 => 1  1이 있기만 하면 1
//Todo: 0 ^ 0 => 0 / 0 ^ 1 => 1 / 1 ^ 1 => 0  1이 하나만 있어야 1, 더하기 연산과 비슷함

const getSum = function (a, b) {
  return b === 0 ? a : getSum(a ^ b, (a & b) << 1);
};

// Different answer
// const getSum = function (a, b) {
//   let carry;
//   while ((a & b) !== 0) {
//     carry = (a & b) << 1;
//     a = a ^ b;
//     b = carry;
//   }
//   return a ^ b;
// };
