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