function spiralOrder(matrix){
  let left = 0;
  let top = 0;
  let right = matrix[0].length - 1;
  let bottom = matrix.length - 1;

  const result = [];

  let direction = 'right';

  while(left <= right && top <= bottom){
    if(direction === 'right'){
      for(let i = left; i <= right; i++){   // we start left to right
        result.push(matrix[top][i]);    // fix the top row and iterate col
      }
      top++;                            // move one row top to bottom
      direction = 'down';
    }

    else if(direction === 'down'){
      for(let i = top; i <= bottom; i++){
        result.push(matrix[i][right]);   // iterate row top to bottom and fix the right col
      }
      right--;                          // move one col right to left
      direction = 'left';
    }

    else if(direction === 'left'){
      for(let i = right; i >= left; i--){
        result.push(matrix[bottom][i]);  // fix the bottom row and iterate col right to left
      }
      bottom--;                           // move one row bottom to top 
      direction = 'up';
    }
    
    else if(direction === 'up'){
      for(let i = bottom; i >= top; i--){
        result.push(matrix[i][left])  // iterate row bottom to top and fix the left col
      }
      left++;                         // move one col left to right
      direction = 'right';
    }
  }
  return result;
}