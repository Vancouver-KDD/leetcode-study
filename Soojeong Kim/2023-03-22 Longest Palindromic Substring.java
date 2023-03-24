class Solution {
    public static int len;
    public String longestPalindrome(String s) {
        int max=Integer.MIN_VALUE;
        String result = "";
        int len = s.length();
        
        //인덱스가 기준점이라고 생각하고
        for(int i=0;i<len;i++) {
            int start = i;
            int end = i;
            //기준점이 있을 때,
            while(start>=0 && end < len) {
                if(s.charAt(start) != s.charAt(end)) {
                    break;
                }else {
                    if(end-start+1>max) {
                        max = end-start +1;
                        result = s.substring(start, end+1);
                    }
                }
                end++;
                start--;
            }
            //기준점이 없을 때
            start = i;
            end = i+1;
            while(start>=0 && end < len) {
                if(s.charAt(start) != s.charAt(end)) {
                    break;
                }else {
                    if(end-start+1 >max) {
                        max = end-start+1;
                        result = s.substring(start, end+1);
                    }
                }
                end++;
                start--;
            }
            
        }
        return result;
    }
    //O(N^2) space O(1)
    public String longestPalindrome2(String s) {
        int n = s.length(), start = 0, end = 0;
        boolean[][] dp = new boolean[n][n];
    
        for (int len=0; len<n; len++) {
            for (int i=0; i+len<n; i++) {
                dp[i][i+len] = s.charAt(i) == s.charAt(i+len) && (len < 2 || dp[i+1][i+len-1]);
                if (dp[i][i+len] && len > end - start) {
                    start = i;
                    end = i + len;
                }
            }
        }
    
        return s.substring(start, end + 1);
    }
    //O(N^2) space O(N^2)
}




