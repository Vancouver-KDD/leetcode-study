var pacificAtlantic = function (heights) {
    if (!heights.length) return heights;
    let row = heights.length, col = heights[0].length, coords = [];
    const peaks = new Array(row * col).fill(0);
  
    const findPeak = (i, j, ocean, prevHeight) => {
      let peakIdx = (i * col) + j;
      if (peaks[peakIdx] === ocean || peaks[peakIdx] === 3 || heights[i][j] < prevHeight) return;
      peaks[peakIdx] += ocean, prevHeight = heights[i][j];
  
      if (peaks[peakIdx] === 3) coords.push([i,j]);
      if (i + 1 < row) findPeak(i + 1, j, ocean, prevHeight);
      if (i > 0) findPeak(i - 1, j, ocean, prevHeight);
      if (j + 1 < col) findPeak(i, j + 1, ocean, prevHeight);
      if (j > 0) findPeak(i, j - 1, ocean, prevHeight);
    }
  
    for (let i = 0; i < row; i++) {
      findPeak(i, 0, 1, heights[i][0]);
      findPeak(i, col - 1, 2, heights[i][col - 1]);
    }
  
    for (let j = 0; j < col; j++) {
      findPeak(0, j, 1, heights[0][j]);
      findPeak(row - 1, j, 2, heights[row - 1][j]);
    }
  
    return coords;
  }
  