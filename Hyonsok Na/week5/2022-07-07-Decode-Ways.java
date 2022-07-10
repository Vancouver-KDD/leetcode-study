class Solution {
    public int numDecodings(String s) {
        if(s.length()==0||s.charAt(0)=='0') return 0;
        else if(s.length()==1&&s.charAt(0)!='0') return 1;
        else{
            int[] dp = new int[s.length()+1];
        dp[0]=1;
        dp[1]=s.charAt(0)=='0'?0:1;
        for(int i=2;i<dp.length;i++){
            if(s.charAt(i-1)!='0') 
                dp[i]+=dp[i-1];
            String db = s.substring(i-2,i);
            if(Integer.valueOf(db)>9&&Integer.valueOf(db)<27)
                dp[i]+=dp[i-2];
        }
           return dp[dp.length-1];
        }
    }
}