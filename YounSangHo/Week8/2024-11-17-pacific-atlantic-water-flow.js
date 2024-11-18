class Solution {
  /**
   * @param {number[][]} heights
   * @return {number[][]}
   */
  pacificAtlantic(heights) {
    // 1. find cell which can flow to both the Pacific and Atlantic
    // 2. Pacific side are top and left
    // 3. Atlantic side are bottom and right
    // 4. water can flow neighboring cell with height equal or lower
    // 5. find a cell bigger height than top or left and bottom or right.

    // [0,0] and [row.length , col.length] are cound't flow both ocean
    //

    let ROWS = heights.length,
      COLS = heights[0].length;
    let pac = Array.from({ length: ROWS }, () => Array(COLS).fill(false));
    let atl = Array.from({ length: ROWS }, () => Array(COLS).fill(false));

    const dfs = (r, c, ocean) => {
      ocean[r][c] = true;
      let directions = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
      ];
      for (let [dr, dc] of directions) {
        let nr = r + dr,
          nc = c + dc;
        if (
          nr >= 0 &&
          nr < ROWS &&
          nc >= 0 &&
          nc < COLS &&
          !ocean[nr][nc] &&
          heights[nr][nc] >= heights[r][c]
        ) {
          dfs(nr, nc, ocean);
        }
      }
    };

    for (let c = 0; c < COLS; c++) {
      dfs(0, c, pac);
      dfs(ROWS - 1, c, atl);
    }
    for (let r = 0; r < ROWS; r++) {
      dfs(r, 0, pac);
      dfs(r, COLS - 1, atl);
    }

    let res = [];
    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        if (pac[r][c] && atl[r][c]) {
          res.push([r, c]);
        }
      }
    }
    return res;
  }
}
