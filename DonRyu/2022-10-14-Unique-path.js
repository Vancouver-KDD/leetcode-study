function numPaths(m, n) {
  const result = [[]];
  // Adding the first row of ’1’s to the array
  for (let i = 0; i < n; i += 1) {
    result[0].push(1);
  }
  // iterating over each of the rows
  for (let i = 1; i < m; i += 1) {
    result.push([1]);    // adding 1 to the first, left most square

      // Getting the total for the current square
    for (let j = 1; j < n; j += 1) {
      result[i][j] = result[i][j - 1] + result[i - 1][j];
    }
  }
// Return the bottom right hand value that has the total.
  return result[m - 1][n - 1];
}
