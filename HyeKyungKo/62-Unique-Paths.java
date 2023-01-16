//2022-12-04
//Time Complexity: O(MxN)
//Space Complexity: O(MxN)
class Solution {
    public int uniquePaths(int m, int n) {
        if(m <=0 || n <= 0){
            return 0;
        }

        int[][] maxPath = new int[m][n];

        for(int i = 0; i < m; i++){
            maxPath[i][0] = 1;
        }

        for(int j = 0; j < n; j++){
            maxPath[0][j] = 1;
        }

        for(int i = 1; i < m; i++){
            for(int j = 1; j <n; j++){
                maxPath[i][j] = maxPath[i-1][j] + maxPath[i][j-1];
            }
        }

        return maxPath[m-1][n-1];
    }
}