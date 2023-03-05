var numIslands = function(grid) {
    let numberofIslands = 0;
    
    //예외처리
    
    if(grid === null || grid.length === 0) return 0;
    
    //깊이우선탐색 이용 알고리즘
    
    for(let row = 0; row<grid.length; row++){
        for(let col =0; col<grid[0].length; col++){
            if(grid[row][col] == "1"){
                numberofIslands++;
                dfs(grid, row, col);
            }        
        }
    }
    

    function dfs (grid, row, col) {
        if(row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] === "0"){
                return 0;
        } //더이상 땅이 아닐 경우는 return
        
        grid[row][col] = "0";
        dfs(grid, row-1, col);
        dfs(grid, row+1, col);
        dfs(grid, row, col-1);
        dfs(grid, row, col+1);
    } //동서 남북을 탐색하는 함수
    
    
    
    return numberofIslands;
    
    
};