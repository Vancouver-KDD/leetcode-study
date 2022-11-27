/**
 * @param {number[]} nums
 * @return {number[]}
 */


// 1. Input의 index 각각 순회 하는 for
// 2. 해당 input에 도달 하였을때 나머지 것들의 product을 구해서 output 안에 넣어 준다

var productExceptSelf = function (nums) {

  let outPut = []

  for (let index = 0; index < nums.length; index++) {

    let sumOfArr = 1
    let arrWithoutIndex = nums.filter((item) => {
      return item !== nums[index]
    })

    arrWithoutIndex.forEach((item) => {
      sumOfArr *= item
    })
    outPut.push(sumOfArr)
  }

  return outPut
};

[0,0]

// a b c d
// 1   a  ab  abc
// bcd cd d    1
// bcd acd abd abc

// 1,2,3,4
// 1  1  2 6
// 24 12 4 1

// 24,12,8,6

var productExceptSelf2 = function (nums) {

  let output = []
  let prefix = 1
  let postfix = 1

  for (let preIndex = 0; preIndex < nums.length; preIndex++) {
    output.push(prefix);
    prefix*=nums[preIndex];
  }

  for (let index = nums.length-1; index >= 0; index--) {

    output[index] *= postfix
    postfix *= nums[index]
  }

  return output
};


console.log(productExceptSelf2([1,2,3,4]))
