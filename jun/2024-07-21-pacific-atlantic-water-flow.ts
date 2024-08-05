function pacificAtlantic(heights: number[][]): number[][] {
    const result: number[][] = []
    const pacific = new Set();
    const atlantic = new Set();
    let i, j;
    const {length: col} = heights;
    const {length: row} = heights[0];

    for(i = 0; i < col; i ++) {
        helper(i, 0, pacific, heights[i][0]);
        helper(i, row - 1, atlantic, heights[i][row - 1])
    }
    for(j = 0; j < row; j++) {
        helper(0, j, pacific, heights[0][j]);
        helper(col - 1, j, atlantic, heights[col - 1][j]);
    }
    for(i = 0; i < heights.length; i++) {
        for(j = 0; j < heights[0].length; j++) {
            if(pacific.has(`${i},${j}`) && atlantic.has(`${i},${j}`)){
                result.push([i,j]);
            }
        }
    }
    function helper(m: number, n: number, visit, prev: number) {
        const curr = heights?.[m]?.[n];
        if(m < 0 || n < 0 || m >= heights.length || n >= heights[0].length || visit.has(`${m},${n}`) || prev > curr) return;

        visit.add(`${m},${n}`)
        helper(m + 1, n, visit, curr);
        helper(m - 1, n, visit, curr);
        helper(m, n + 1, visit, curr);
        helper(m, n - 1, visit, curr);
    }
    return result;
};
