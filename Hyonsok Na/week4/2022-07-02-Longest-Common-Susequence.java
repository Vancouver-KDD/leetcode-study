// using recursion tree we can understand more clearly
// TC o(m*n)
// sc o(m*n)
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m=text1.length();
        int n=text2.length();
        
        int[][] dp = new int[m][n];
        for(int[] el: dp){
            Arrays.fill(el,-1);
        }
        
        return getLCS(m-1,n-1,text1,text2,dp);
    }
    
   
    // we are starting from last index of both char
    private int getLCS(int index1, int index2, String text1, String text2,int[][] dp){
        
        if(index1<0 || index2<0){
            return 0;
        }
        
        if(dp[index1][index2]!=-1){
            return dp[index1][index2];
        }
        
         // here we are checking if both char with index are match we are returning 1+ function call  
         // here we are decreasing index on both side beacause it maches
         // we are adding 1 in ans beacuse 1 char matches 
        if(text1.charAt(index1)==text2.charAt(index2)){
            return dp[index1][index2]= 1+getLCS(index1-1,index2-1,text1,text2,dp);
        }
        
        // if not maches we are using 2 case decraesing index one by one from both index and compare
        // decrease index1-1 only other is same 
        // decraese index2-1 only other is same
        // taking max between them
         return dp[index1][index2]=  0 + Math.max( getLCS(index1,index2-1,text1,text2,dp), getLCS(index1-1,index2,text1,text2,dp));
                
    }
    
}