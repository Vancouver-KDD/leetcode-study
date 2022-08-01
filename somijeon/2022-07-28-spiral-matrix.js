// Given an m x n matrix, return all elements of the matrix in spiral order.

// Ex 1:

// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [1,2,3,6,9,8,7,4,5]

// Ex 2:

// Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
// Output: [1,2,3,4,8,12,11,10,9,5,6,7]

var spiralOrder = function (matrix) {
  if (!matrix.length) return [];
  const result = [];
  const directions = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  const range = [matrix[0].length, matrix.length - 1];
  let d = 0,
    r = 0,
    c = -1;
  while (range[d % 2] > 0) {
    for (let i = 0; i < range[d % 2]; i++) {
      r += directions[d][0];
      c += directions[d][1];
      result.push(matrix[r][c]);
    }
    range[d % 2]--;
    d = (d + 1) % 4;
  }
  return result;
};
