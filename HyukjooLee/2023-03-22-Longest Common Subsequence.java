// Given two strings text1 and text2, return the length of their longest common subsequence. 
// If there is no common subsequence, return 0.

// A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted 
// without changing the relative order of the remaining characters.

// For example, "ace" is a subsequence of "abcde".
// A common subsequence of two strings is a subsequence that is common to both strings.

// Input: text1 = "abcde", text2 = "ace" 
// Output: 3  
// Explanation: The longest common subsequence is "ace" and its length is 3.


// text1 과 text2 에 대한 LCS 를 찾는 문제
// a common string to both strings in relative order
// "ABCD" <--> "AEFD"
// => AD 
// "AGGTAB" <--> "GXTXAYB"
// => GTAB

// finding for the length of LCS => we can divide the a problem into smaller problems
// 하위 문제에 대한 솔루션을 결합하여 전체 문제에 대한 솔루션을 얻을 수 있을 때 dp 가 적합
// 1. initialize dp array (m+1) x (n+1); lengths of text1 and text2
// 2. if text1[i-1] == text2[j-1], dp[i][j] = dp[i-1][j-1] + 1
// else, dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
// 현재 어떤 substring이 가장 긴 공통 하위 시퀀스를 제공할지 모르기 때문에 두 길이 중 최대값
// time complexity is O(MN): the lengths of the input strings
// space complexity is also O(MN): to store the 2D array dp
public static int longestCommonSubsequence(String text1, String text2) {
    int len1 = text1.length(), len2 = text2.length();

    
    int[][] dp = new int[len1 + 1][len2 + 1];
    for (int i = 0; i <= len1; i++) {
        dp[i][0] = 0;
    }
    for (int j = 0; j <= len2; j++) {
        dp[0][j] = 0;
    }

    // Fill up dp array
    for (int i = 1; i <= len1; i++) {
        for (int j = 1; j <= len2; j++) {
            if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    // Return length of longest common subsequence
    return dp[len1][len2];
}


// using 1-D array
// reduces the space complexity
// O(min(M,N)): the lengths of text1 and text2
public static int longestCommonSubsequence(String text1, String text2) {
    int len1 = text1.length(), len2 = text2.length();

    // Make len1 <= len2 to reduce space complexity
    if (len1 > len2) {
        String temp = text1;
        text1 = text2;
        text2 = temp;
        int tempLen = len1;
        len1 = len2;
        len2 = tempLen;
    }

    // Initialize dp array
    int[] dp = new int[len1 + 1];
    int prev, temp;

    // Fill up dp array
    for (int j = 1; j <= len2; j++) {
        prev = 0;
        for (int i = 1; i <= len1; i++) {
            temp = dp[i];
            if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                dp[i] = prev + 1;
            } else {
                dp[i] = Math.max(dp[i - 1], dp[i]);
            }
            prev = temp;
        }
    }

    // Return length of longest common subsequence
    return dp[len1];
}
