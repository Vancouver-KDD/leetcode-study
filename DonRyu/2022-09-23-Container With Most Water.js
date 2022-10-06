//brutal
var maxAreaB = function (height) {
  let sum;
  let maxSum = 0;

  for (let a = 0; a < height.length; a++) {
    for (let b = 1; b < height.length; b++) {
      sum = (b - a) * Math.min(height[a], height[b])
      maxSum = Math.max(maxSum, sum)
    }
  }
  return maxSum;
};

const maxArea = (height) => {
  let res = 0;
  let left = 0;
  let right = height.length - 1

  while (left < right) {
    let area = (right - left) * Math.min(height[left], height[right])
    res = Math.max(res, area)

    if (height[left] < height[right]) {
      left += 1
    } else if (height[left] > height[right]) {
      right -= 1
    } else {
      right -= 1
    }
  }
  return res
}

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
