// [1, 2, 3]
// [4, 5, 6]
// [7, 8, 9]


function rotate(matrix){
  for(let i = 0; i < matrix.length; i++){
    for(let j = i + 1; j < matrix[0].length; j++){
      temp = matrix[j][i];  //[1][0] 2
      matrix[j][i] = matrix[i][j]; // 2 --> 4
      matrix[i][j] = temp;  // 4 --> 2
    }
  }

  for(let row of matrix){
    row.reverse();
  }
}