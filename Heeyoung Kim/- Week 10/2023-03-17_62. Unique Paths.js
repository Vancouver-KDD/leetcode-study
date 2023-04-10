/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
 var uniquePaths = function(m, n) {
    let matrix = [];
   
   for(let row=1; row<=n; row++){
       matrix.push([]);
   }
   
   for(let row=0; row<n; row++){
       matrix[row][0] = 1;
   }
   
   for(let col=1; col<m; col++){
       matrix[0][col] = 1;
   }
   
   for(let row=1; row<n; row++){
       for(let col=1; col<m; col++){
           matrix[row][col] = matrix[row][col-1] + matrix[row-1][col];
       }
   }
   
   return matrix[matrix.length-1][m-1];
};