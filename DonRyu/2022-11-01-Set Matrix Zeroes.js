const setZeroes = function(matrix) {
    let col0 = 1, row = matrix.length, col = matrix[0].length;

    for(let i = 0; i < row; i++) {
        if(matrix[i][0] === 0) col0 = 0;
        for(let j = 1; j < col; j++) {
            if(matrix[i][j] === 0) {
                matrix[i][0] =  matrix[0][j] = 0;
            }
        }
    }

    for(let i = row-1; i >= 0; i--) {
        for(let j = col-1; j > 0; j--) {
            if(matrix[i][0] === 0 || matrix[0][j] === 0) matrix[i][j] = 0;
        }
        if(col0 === 0) matrix[i][0] = 0;
    }
};
