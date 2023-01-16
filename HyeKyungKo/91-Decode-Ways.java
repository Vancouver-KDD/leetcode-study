
//Input:  s="12"  -> output: 2  (AB(1 2), L(12))
//Input : s="226" -> output: 3 (BZ(2 26), VF(22 6), BBF(2 2 6))
//Input : s="10"  -> output: 1 ( J(10))
//Input : s="101" -> output: 2 ( J(10), A(1))
//Input : s= "99" -> output: 1 (I(9), I(9))
//Input : s="909" -> output: 0 (no valid value)
//Input : s="05" -> output: 0 ( no valid value)

//나중에 recursive 로도 해보기 
//2022-12-04 -iteration 
//Time Complexity: O(N)
//Space Complexity: O(1)
//현재까지 나올수 있는 경우의 수 는 현재 숫자를 1개의 alpahbet 으로 보는 경우의 수  ( i-1 까지의 경우의 수를 가져오면됨)
// 더하기, i-1, i 번째 2개의 숫자로 하나의 alphabet 을 만드는 경우의 수 ( i-2 까지의 경우의 수를 가져오면 됨)

class Solution {
    public int numDecodings(String s) {
        if(s == null || s.length() == 0){
            return 0;
        }

        if(s.charAt(0) == '0'){
            return 0;
        }
        int prevPrev = 1;
        int prev = 1;
        int max = 0;
        for(int i = 1; i < s.length(); i++){

            if(s.charAt(i) == '0'){
                max = 0;
            }else{
                max = prev;
            }

            if(s.charAt(i-1) != '0'){
                int number = (ch - '0') + (s .charAt(i-1) -'0') * 10;
                if(number <= 26){
                    max += prevPrev;
                }
            }

            prevPrev = prev;
            prev = max;
        }

        return max;
    }
}

//리트코드 솔루션
/*
//Time Complexity: O(N)
//Space Complxity: O(1)
class Solution {
    public int numDecodings(String s) {  
        if (s.charAt(0) == '0') {
            return 0;
        }

        int n = s.length();
        int twoBack = 1;
        int oneBack = 1;
        for (int i = 1; i < n; i++) {
            int current = 0;
            if (s.charAt(i) != '0') {
                current = oneBack;
            }
            int twoDigit = Integer.parseInt(s.substring(i - 1, i + 1));
            if (twoDigit >= 10 && twoDigit <= 26) {
                current += twoBack;
            }
           
            twoBack = oneBack;
            oneBack = current;
        }
        return oneBack;
    }
}
*/
/*
//Time Complexity: O(N)
//Space Complexity: O(N)
class Solution {

    public int numDecodings(String s) {
        // DP array to store the subproblem results
        int[] dp = new int[s.length() + 1];
        dp[0] = 1;
        
        // Ways to decode a string of size 1 is 1. Unless the string is '0'.
        // '0' doesn't have a single digit decode.
        dp[1] = s.charAt(0) == '0' ? 0 : 1;

        for(int i = 2; i < dp.length; i++) {
            // Check if successful single digit decode is possible.
            if (s.charAt(i - 1) != '0') {
               dp[i] = dp[i - 1];  
            }
            
            // Check if successful two digit decode is possible.
            int twoDigit = Integer.valueOf(s.substring(i - 2, i));
            if (twoDigit >= 10 && twoDigit <= 26) {
                dp[i] += dp[i - 2];
            }
        }
        
        return dp[s.length()];
    }
}
*/