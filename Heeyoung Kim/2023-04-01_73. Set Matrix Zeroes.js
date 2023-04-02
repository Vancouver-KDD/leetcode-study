var setZeroes = function(matrix) {
    let fistcolhaszero = false;
    let firstrowhaszero = false;
    
    // check it there is zero in first col & row
    
    for(let i =0; i<matrix.length; i++){
        if(matrix[i][0] === 0){
            fistcolhaszero = true;
            break;
        }
    }
    for(let i =0; i<matrix[0].length; i++){
        if(matrix[0][i] === 0){
            firstrowhaszero = true;
            break;
        }
    }
    
    
    
    //use first row and col as flags, if rest of cells have zeros 
    for(let row = 1; row<matrix.length; row++){
        for(let col =1; col<matrix[0].length; col++){
            if(matrix[row][col]=== 0){
                matrix[0][col] = 0;
                matrix[row][0] = 0;
            }
        }
    }
    
    
    //zero out cells based on flags in first row and column.
    for(let row = 1; row<matrix.length; row++){
        for(let col =1; col<matrix[0].length; col++){
            if(matrix[row][0]=== 0 || matrix[0][col] === 0){
                matrix[row][col] = 0;    
            }
        }
    }
    
    
     //Zero out first column
    if(fistcolhaszero) {
        for(let i=0; i<matrix.length; i++){
            matrix[i][0] = 0;
        }
    }
    
    
    
    //Zero out first row

    if(firstrowhaszero) {
        for(let i=0; i<matrix[0].length; i++){
            matrix[0][i] = 0;
        }
    }
    
    
    
};