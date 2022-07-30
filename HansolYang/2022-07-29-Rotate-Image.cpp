class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.size() <= 1) {
            return;
        }
        
        int n = matrix.size() - 1;
        
        vector<vector<int>> temp = matrix;
        
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                matrix[j][n-i] = temp[i][j];
            }
        }
        
    }
};