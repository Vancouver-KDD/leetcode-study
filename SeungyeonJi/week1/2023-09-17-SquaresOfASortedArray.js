var sortedSquares = function (nums) {
  let arr = [];
  nums.map((num) => arr.push(num ** 2));
  return arr.sort((a, b) => a - b);
};
