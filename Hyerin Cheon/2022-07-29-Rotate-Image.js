// [1, 2, 3]
// [4, 5, 6]
// [7, 8, 9]


function rotate(matrix){
  for(let i = 0; i < matrix.length; i++){
    for(let j = i + 1; j < matrix[0].length; j++){
      temp = matrix[j][i];  //[1][0] 4
      matrix[j][i] = matrix[i][j]; // 4 --> 2
      matrix[i][j] = temp;  // 2 --> 4
    }
  }

  for(let row of matrix){
    row.reverse();
  }
}