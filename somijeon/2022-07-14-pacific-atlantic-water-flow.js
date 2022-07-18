var pacificAtlantic = function (heights) {
  let res = [];
  let min = -Infinity;
  let rows = heights.length;
  let cols = heights[0].length;
  let pacific = new Array(rows).fill().map(() => new Array(cols).fill(0));
  let atlantic = new Array(rows).fill().map(() => new Array(cols).fill(0));

  for (let row = 0; row < rows; row++) {
    dfs(heights, row, 0, min, pacific);
    dfs(heights, row, heights[0].length - 1, min, atlantic);
  }
  for (let col = 0; col < cols; col++) {
    dfs(heights, 0, col, min, pacific);
    dfs(heights, heights.length - 1, col, min, atlantic);
  }

  for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
      if (pacific[row][col] == 1 && atlantic[row][col] == 1) {
        res.push([row, col]);
      }
    }
  }
  return res;
};

const dfs = (heights, r, c, prevVal, ocean) => {
  // 1. Check necessary condition.
  if (r < 0 || c < 0 || r > heights.length - 1 || c > heights[0].length - 1) return;
  if (heights[r][c] < prevVal) return;
  if (ocean[r][c] == 1) return;

  // 2. Process call.
  ocean[r][c] = 1;

  // 3. Call dfs as needed.
  dfs(heights, r - 1, c, heights[r][c], ocean);
  dfs(heights, r + 1, c, heights[r][c], ocean);
  dfs(heights, r, c - 1, heights[r][c], ocean);
  dfs(heights, r, c + 1, heights[r][c], ocean);
};
