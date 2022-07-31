class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        int low_n = 0;
        int upr_n = matrix.size(); //number of rows
        int low_m = 0;
        int upr_m = matrix[0].size(); //number of columns
        int total = upr_n*upr_m;
        
        int col = low_m;
        int row = low_n;
        
        vector<int> res;
        
        while (res.size() < total) {
            res.push_back(matrix[row][col]);
            if (row == low_n) {
                if (col != upr_m - 1) {
                    col++;
                } else {
                    low_n++;
                    row++;
                }
            } else if (col == upr_m) {
                if (row != upr_n) {
                    row++;
                } else {
                    upr_m--;
                    col--;
                }
            } else if (row == upr_n) {
                if (col != low_m) {
                    col--;
                } else {
                    upr_n--;
                    row--;
                }
            } else {
                if (row != low_n) {
                    row--;
                } else {
                    low_n++;
                    col++;
                }
            }
        }
        
        return res;
    }
};