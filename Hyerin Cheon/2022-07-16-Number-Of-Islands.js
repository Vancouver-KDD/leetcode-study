var numIslands = function (grid){
  // number of counted island
  let countIsland = 0;

  for(let row = 0; row < grid.length; row++){
    for(let col = 0; col < grid[row].length; col++){
      if(grid[row][col] == '1'){
        countIsland ++;
        explore(row, col, grid);
      }
    }
  }
  return countIsland;
}

// convert stuff around us to water('0')
function explore(row, col, grid){
  // if row is out of bounds
  // if col is out of bounds
  // dont want to change water('0') to water('0')
  if(grid[row] === undefined || grid[row][col] === undefined || grid[row][col] === '0' ){
    // not execute
    return;
  }
  // change current spot to '0'
  grid[row][col] = '0'

  // explore right, left, down, and top
  explore(row, col + 1, grid)   // right
  explore(row, col - 1, grid)   // left
  explore(row + 1, col, grid)   // down
  explore(row - 1, col, grid)   // top
}