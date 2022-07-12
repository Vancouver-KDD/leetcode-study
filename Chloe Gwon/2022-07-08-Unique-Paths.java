class Solution {
    public int uniquePaths(int m, int n) {

        int count[][] = new int[m][n];
        
        for (int i=0; i<m; i++){
            count[i][0] = 1;
        }
        for (int j=0; j<n; j++){
            count[0][j] = 1;
        }
        
        for (int i=1; i<m; i++){
            for (int j=1; j<n; j++){
                count[i][j] = count[i][j-1] + count[i-1][j];
            }
        }
        
        return count[m-1][n-1];
    }
}
