// You are given an n x n 2D matrix representing an image,
//todo: rotate the image by 90 degrees (clockwise).

// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

var rotate = function (matrix) {
  let col = 1;
  for (let i = 0; i < matrix.length; i++) {
    for (let j = col++; j < matrix[0].length; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
    }
  }
  for (let r of matrix) {
    r.reverse();
  }
};
