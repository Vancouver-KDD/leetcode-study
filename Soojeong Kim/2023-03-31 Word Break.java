import java.util.*;
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int len = s.length();
        boolean [] dp = new boolean[len];

        for(int i = 0; i<len;i++) {
            for(int j = 0; j <=i;j++) {
                String temp = s.substring(j, i+1);

                if(wordDict.contains(temp) && (j == 0 || dp[j-1])) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[len-1];
    }
}
//TC : O(N^3) 
/*
 The for loop is looking at ranges or substrings. If we know that the current substring is in the dictionary AND the substring before it is also in the dictionary then we know that the str.substring(0, i) is true. J == 0 because the first substring has nothing before it (dp[j- 1] does not exist).

------- left substring ---- | substring (j, i + 1) | -------right substring ------ |

If we know that str.substring(j,i+1) is in the dictionary, we can only mark it true if the left substring is also in the dictionary.
Then, for the right substring, it is str.substring(i + 1, end). You can only mark dp[end] is true if you know the substring up to i are in dictionary.
This is what makes this a dynamic programming solution.
 */