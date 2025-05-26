class Solution {
  /**
   * @param {number[][]} matrix
   * @param {number} target
   * @return {boolean}
   */
  searchMatrix(matrix, target) {
    let startRow = 0;
    let endRow = matrix.length - 1;
    let startCols = 0;
    let endCols = 0;
    let cols = null;

    if (endRow === 0) {
      cols = matrix[0];
    } else {
      while (startRow <= endRow) {
        let mid = Math.floor((startRow + endRow) / 2);
        let midFirst = matrix[mid][0];
        let midEnd = matrix[mid][matrix[mid].length - 1];

        if (matrix[mid][0] === target) {
          return true;
        }

        if (midFirst <= target && target <= midEnd) {
          cols = matrix[mid];
          break;
        } else if (target < midFirst) {
          endRow = mid - 1;
        } else if (midEnd < target) {
          startRow = mid + 1;
        }
      }
    }

    if (cols) {
      endCols = cols.length - 1;
      while (startCols <= endCols) {
        let midCols = Math.floor((startCols + endCols) / 2);

        if (cols[midCols] === target) {
          return true;
        } else if (cols[midCols] > target) {
          endCols = midCols - 1;
        } else {
          startCols = midCols + 1;
        }
      }
    }

    return false;
  }
}
