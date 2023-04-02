var spiralOrder = function(matrix) {
    let arr = []
    let r = matrix.length;
    let c = matrix[0].length;
    let direction = 0;
    let left = 0;
    let right = c-1;
    let bottom = 0;
    let top = r-1;

    while(arr.length<r*c){
        if(direction == 0){
            for(let i = left; i<=right; i++){
                arr.push(matrix[bottom][i])
            }
            bottom++
            direction++
        }
        else if(direction == 1){
            for(let i = bottom; i<=top; i++){
                arr.push(matrix[i][right])
            }
            right--
            direction++
        }
        else if(direction == 2){
            for(let i = right; i>=left;i--){
                arr.push(matrix[top][i])
            }
            top--
            direction++
        }
        else if(direction==3){
            for(let i =top; i>=bottom; i--){
                arr.push(matrix[i][left])
            }
            left++
            direction++
        }
        if(direction == 4) direction = 0;
    }
    return arr;
};