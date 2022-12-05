// const twoSum = function (nums, target) {
//
//   for (let a = 0; a < nums.length; a++) {
//
//     let index0 = a;
//
//     for (let b = 0; b < nums.length; b++) {
//
//       let index1 = b;
//
//       if (a !== b && nums[a] + nums[b] === target) {
//         return [index0, index1]
//       }
//     }
//   }
// };

// console.log(twoSum([3, 3], 6))

// [6,1,2,4] 3

let map = new Map()

const twoSumMap = (nums, target) => {
  for (let a = 0; a < nums.length; a++) {
    let value = target - nums[a]
    if (map.has(value)) {
      return [map.get(value), a]
    } else {
      map.set(nums[a], a)
    }
  }
}

const twoSum = (nums, target) => {
  for (let index = 0; index < nums.length; index++) {
    let remainValue = target - nums[index]
    if (map.has(remainValue)) {
      return [map.get(remainValue), index]
    } else {
      map.set(nums[index], index)
    }
  }
}

console.log(twoSum([3, 3], 6))
