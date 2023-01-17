// intuitive
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        vector<int> row(m,1);
        vector<int> col(n,1);
        
        // iterate and find zeros
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(matrix[i][j]==0){
                    row[i] = 0;
                    col[j] = 0;
                }
            }
        }
        
        // iterate and set zeros
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(row[i]==0 || col[j]==0){
                    matrix[i][j] = 0;
                }
            }
        }
    }
};