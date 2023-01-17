// transpose => horizontal reflection
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // transpose
        for(int i=0; i<matrix.size(); i++){
            for(int j=0; j<i; j++){
                swap(matrix[i][j], matrix[j][i]);
            }
        }
        // flip
        for(int i=0; i<matrix.size(); i++){
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};

// vertical flip => transpose
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        // flip
        reverse(matrix.begin(), matrix.end());
        // transpose
        for(int i=0; i<matrix.size(); ++i){
            for(int j=i+1; j<matrix[i].size(); ++j){
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};

// swaps
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int a=0, b=matrix.size()-1;
        while(a<b){
            for(int i=0; i<(b-a);++i){
                swap(matrix[a][a+i], matrix[a+i][b]);
                swap(matrix[a][a+i], matrix[b][b-i]);
                swap(matrix[a][a+i], matrix[b-i][a]);
            }
            ++a;--b;
        }
    }
};