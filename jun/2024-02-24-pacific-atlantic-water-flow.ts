function pacificAtlantic(heights: number[][]): number[][] {
  const pacific = new Set()
  const atlantic = new Set()

  for(let r = 0; r < heights.length; r++){
      dfs(pacific, r, 0, heights, 0)
      dfs(atlantic, r, heights[0].length - 1, heights, 0)
  }
  for(let c = 0; c < heights[0].length; c++){
      dfs(pacific, 0, c, heights, 0)
      dfs(atlantic, heights.length - 1, c, heights, 0)
  }
  const result: number[][] = []
  for(let r = 0; r < heights.length; r++){
      for (let c = 0; c < heights[r].length; c++){
          if(pacific.has(`[${r},${c}]`) && atlantic.has(`[${r},${c}]`)){
              result.push([r,c])
          }
      }
  }
  return result
};

function dfs(visit, r: number, c: number, heights: number[][], prevHeight: number) {
  if(r < 0 || c < 0 || r >= heights.length || c >= heights[0].length || visit.has(`[${r},${c}]`) || heights[r][c] < prevHeight) {
      return
  }
  const curr = heights[r][c]
  visit.add(`[${r},${c}]`)
  dfs(visit, r - 1, c, heights, curr)
  dfs(visit, r + 1, c, heights, curr)
  dfs(visit, r, c - 1, heights, curr)
  dfs(visit, r, c + 1, heights, curr)
}