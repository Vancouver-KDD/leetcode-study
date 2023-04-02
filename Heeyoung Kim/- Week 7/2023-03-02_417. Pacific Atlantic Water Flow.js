var pacificAtlantic = function(heights) {
    if (!heights.length) return heights
    let y = heights.length, x = heights[0].length, answer = [],
        dp = new Uint8Array(x * y)
    const dfs = (i, j, w, h) => {
        let ij = i * x + j
        if ((dp[ij] & w) || heights[i][j] < h) return
        dp[ij] += w, h = heights[i][j]
        if (dp[ij] === 3) answer.push([i,j])
        if (i + 1 < y) dfs(i+1, j, w, h)
        if (i > 0) dfs(i-1, j, w, h)
        if (j + 1 < x) dfs(i, j+1, w, h)
        if (j > 0) dfs(i, j-1, w, h)
    }   
    for (let i = 0; i < y; i++) {
        dfs(i, 0, 1, heights[i][0])
        dfs(i, x-1, 2, heights[i][x-1])
    }
    for (let j = 0; j < x; j++) {
        dfs(0, j, 1, heights[0][j])
        dfs(y-1, j, 2, heights[y-1][j])
    }
    return answer
};