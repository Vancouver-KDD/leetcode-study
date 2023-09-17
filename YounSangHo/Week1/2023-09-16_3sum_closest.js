/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
  let result = null;

  // 주어진 숫자 배열에서 3개 숫자를 선택하는 모든 조합
  for (let i = 0; i < nums.length - 2; i++) {
    for (let j = i + 1; j < nums.length - 1; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        const sum = nums[i] + nums[j] + nums[k];
        const distance = target - sum;
        if (square(target - result) > square(distance) || result === null) {
          result = sum;
        }
      }
    }
  }

  return result;
};

// 제곱 계산
const square = (num) => num * num;
