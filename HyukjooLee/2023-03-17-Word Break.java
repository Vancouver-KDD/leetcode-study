// Given a string s and a dictionary of strings wordDict, 
// return true if s can be segmented into a space-separated sequence of one or more dictionary words.

// Note that the same word in the dictionary may be reused multiple times in the segmentation.

// Input: s = "leetcode", wordDict = ["leet","code"]
// Output: true
// Explanation: Return true because "leetcode" can be segmented as "leet code".

// using DP to determine if a given string can be segmented
// boolean array; indicates that the substring s[0:i] can be segmented
// time complexity of this algorithm is O(n^2): the length of the string
// each index in the string O(N) * O(N)-substring check O(n) time
// space complexity is O(N) - an array dp
public boolean wordBreak(String s, List<String> wordDict) {
    int n = s.length();
    
    boolean[] dp = new boolean[n+1];
    
    // the empty string can always be segmented 
    dp[0] = true;
    
    // traverse the each char in the string 
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < i; j++) {
            // check if the substring can be segmented into words
            // and whether the remaining substring
            if (dp[j] && wordDict.contains(s.substring(j, i))) {
                dp[i] = true;
                break;
            }
        }
    }
    
    return dp[n];
}
