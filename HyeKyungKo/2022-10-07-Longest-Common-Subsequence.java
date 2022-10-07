//2022.10.07
//limitation : if text1 or text2 is null, return 0
//Time complexity: O( m*n) <- m is text1.length(), n is text2.length()
//Space Complexit : O( m*n)  <-- checkMatrix size
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
     
        if(text1 == null || text1.length() == 0 || text2 == null || text2.length() == 0){
            return 0;
        }
        
        int length1 = text1.length();
        int length2 = text2.length();
            
        int[][] checkMatrix = new int[length1 + 1][length2 + 1];
        
        for(int i = length1-1 ; i >= 0; i--){
            for(int j = length2-1 ; j >= 0; j--){
                if(text1.charAt(i) == text2.charAt(j)){ 
                    checkMatrix[i][j] = checkMatrix[i+1][j+1] + 1;
                }else{
                    checkMatrix[i][j] = Math.max(checkMatrix[i+1][j], checkMatrix[i][j+1]);
                }
            }
        }
          
        return checkMatrix[0][0];
    }
}