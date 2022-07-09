class Solution {
public:
    int uniquePaths(int m, int n) {
        
        double res = 1;
        
        // nCr
        // select minimum paths able to take (right/down) from total
        for(int i=1; i<min(n,m); i++){
            res = res*(n+m-i-1)/i;
        }
        return (int)res;
    }
};
