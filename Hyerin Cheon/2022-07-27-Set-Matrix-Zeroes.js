// find zero with for loop and push to empty array -> keep the row and col fixed 
// -> with helper function, update to zero with fixed and i variable

function setZeroes(matrix){
  const zeroArray = [];
  
  // find zero
  for(let i = 0; i < matrix.length; i++){
    for(let j = 0; j < matrix[0].length; j++){
      if(matrix[i][j] === 0){
        zeroArray.push([i, j])
      }
    }
  }

  // keep the row, col fixed
  for(address of zeroArray){
    let row = address[0];
    let col = address[1];
    updateToZero(row, col, matrix);
  }
}

function updateToZero(r, c, matrix){
  // iterate row value, so col need to be fixed
  for(let i = 0; i < matrix.length; i++){
    matrix[i][c] = 0;
  }

  // iterate col value, so row need to be fixed
  for(let i = 0; i < matrix[0].length; i++){
    matrix[r][i] = 0;
  }
}