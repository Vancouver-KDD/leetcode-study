function uniquePath(m, n){
  // create table
  const table = Array.from({length:m}, () => new Array(n));

  // fill in 1 on the first row
  for(let i = 0; i < table.length; i++) table[i][0] = 1;
  // fill in 1 on the first column
  for(let i = 0; i < table[0].length; i++) table[0][i] = 1;

  for(let i = 1; i < m; i++){           // m = table.length
    for(let j = 1; j < n; j++){         // n = table[0].length
      table[i][j] = table[i-1][j] + table[i][j-1];
    }
  }
  return table[m - 1][n - 1];
}