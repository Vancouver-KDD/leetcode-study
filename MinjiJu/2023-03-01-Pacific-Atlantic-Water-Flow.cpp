class Solution {
public:
    
    void dfs(int i, int j, vector<vector<int>>& height, vector<vector<bool>>& ocean){
        
        int n=height.size(), m=height[0].size();
        
        if(!ocean[i][j]){
            ocean[i][j] = true;
            
            if(i>0 && height[i-1][j]>=height[i][j] && !ocean[i-1][j]) dfs(i-1,j,height,ocean);
            if(j>0 && height[i][j-1]>=height[i][j] && !ocean[i][j-1]) dfs(i,j-1,height,ocean);
            if(i<n-1 && height[i+1][j]>=height[i][j] && !ocean[i+1][j]) dfs(i+1,j,height,ocean);
            if(j<m-1 && height[i][j+1]>=height[i][j] && !ocean[i][j+1]) dfs(i,j+1,height,ocean);
        } 
        return;
    }
    
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        
        vector<vector<int>> res;
        int n=heights.size(), m=heights[0].size();
        
        vector<vector<bool>> pacific(n+1, vector<bool>(m+1,false));
        vector<vector<bool>> atlantic(n+1, vector<bool>(m+1,false));
        
        // check edges of pacific ocean
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(i==0 || j==0) dfs(i,j,heights,pacific);
            }
        }
        
        // check edges of atlantic ocean
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(i==n-1 || j==m-1) dfs(i,j,heights,atlantic);
            }
        }
        
        // if water can flow from both pacific and atlantic, add to res
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(atlantic[i][j] && pacific[i][j]) res.push_back({i,j});
            }
        }
        return res;
    }
};
