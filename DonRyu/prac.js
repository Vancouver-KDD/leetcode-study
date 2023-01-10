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

[0, 0]

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
    prefix *= nums[preIndex];
  }

  for (let index = nums.length - 1; index >= 0; index--) {

    output[index] *= postfix
    postfix *= nums[index]
  }

  return output
};


var findMedianSortedArrays = function (nums1, nums2) {

  let combinedArr = [...nums1, ...nums2]

  function compare(a, b) {
    return a - b
  }

  combinedArr.sort(compare)
  if (combinedArr.length % 2 !== 0) {
    return combinedArr[Math.floor(combinedArr.length / 2)]
  } else {
    let index = (combinedArr.length - 1) / 2
    return (combinedArr[Math.ceil(index)] + combinedArr[Math.floor(index)]) / 2
  }

};

// console.log(findMedianSortedArrays([3], [-1,-2]))


class Car {

  constructor(tire, engine, brand) {
    this.tire = tire
    this.engine = engine
    this.brand = brand
  }

  brandName() {
    return 'Car brand is ' + this.brand
  }
}

class Tesla extends Car {
  constructor(test) {
    super(1,2,'brand');
    this.test =  test
  }

  price() {
    return 'this is the price' + this.brand + this.test
  }
}


let car = new Car(4, 'V8', 'Tesla')
let modelX = new Tesla(9999)


// console.log(car.brandName())
// console.log(modelX.price())


let map = new Map()

map.set('key','value')
console.log(map.get('key'))
console.log(map.has('12'))
