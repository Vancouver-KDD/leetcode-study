function pacificAtlantic(heights: number[][]): number[][] {
  const m = heights.length;
  const n = heights[0].length;

  const pacific = new Set<string>();
  const atlantic = new Set<string>();

  const directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];

  function dfs(r: number, c: number, visited: Set<string>, prevHeight: number) {
    if (r < 0 || c < 0 || r >= m || c >= n) return;
    const key = `${r},${c}`;
    if (visited.has(key)) return;
    if (heights[r][c] < prevHeight) return;

    visited.add(key);

    for (const [dr, dc] of directions) {
      dfs(r + dr, c + dc, visited, heights[r][c]);
    }
  }

  for (let c = 0; c < n; c++) {
    dfs(0, c, pacific, heights[0][c]);
    dfs(m - 1, c, atlantic, heights[m - 1][c]);
  }
  for (let r = 0; r < m; r++) {
    dfs(r, 0, pacific, heights[r][0]);
    dfs(r, n - 1, atlantic, heights[r][n - 1]);
  }

  const result: number[][] = [];
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      const key = `${r},${c}`;
      if (pacific.has(key) && atlantic.has(key)) {
        result.push([r, c]);
      }
    }
  }

  return result;
}
