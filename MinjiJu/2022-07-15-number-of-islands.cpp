class Solution {
public:
    
    void dfs(vector<vector<char>>& grid, vector<vector<bool>>& visited, int i, int j, int n, int m){
        
        if(i<0 || j<0 || i>(n-1) || j>(m-1) || visited[i][j] || grid[i][j]=='0') return;
        
        if(grid[i][j]=='1' && !visited[i][j]){
            visited[i][j] = true;
            dfs(grid, visited, i+1, j, n, m);
            dfs(grid, visited, i-1, j, n, m);
            dfs(grid, visited, i, j+1, n, m);
            dfs(grid, visited, i, j-1, n, m);        
        }
    }
    
    int numIslands(vector<vector<char>>& grid) {
        
        int n=grid.size(), m=grid[0].size();
        vector<vector<bool>> visited(n, vector<bool>(m,false));
        
        int res = 0;
        
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(grid[i][j]=='1' && !visited[i][j]){
                    visited[i][j] = true;
                    dfs(grid, visited, i+1, j, n, m);
                    dfs(grid, visited, i-1, j, n, m);
                    dfs(grid, visited, i, j+1, n, m);
                    dfs(grid, visited, i, j-1, n, m);
                    res++;
                }
            }
        }
        return res;
    }
};