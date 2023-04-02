// A message containing letters from A-Z can be encoded into numbers using the following mapping:

// 'A' -> "1"
// 'B' -> "2"
// ...
// 'Z' -> "26"

// Input: s = "12"
// Output: 2
// Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

// 1. using dp

// time complexity is O(N); the length of the input string.
// space complexity is also O(N); an array dp of length n+1 to store the number of ways to decode
public int numDecodings(String s) {
    int n = s.length();
    
    int[] dp = new int[n+1];
    
    dp[0] = 1;
    
    // it cannot be decoded
    if (s.charAt(0) == '0') {
        return 0;
    }
    
    // can be decoded in only one way
    dp[1] = 1;
    
    for (int i = 2; i <= n; i++) {
        // if the character can be decoded as a digit, we add the number of ways
        if (s.charAt(i-1) != '0') {
            // to decode the substring
            dp[i] += dp[i-1];
        }
        
        // if the current character can be decoded as a two digit
        // then we add the number of ways to decode the substring s[0:i-2] to dp[i]
        int twoDigit = Integer.parseInt(s.substring(i-2, i)); // with the previous one
        if (twoDigit >= 10 && twoDigit <= 26) {
            dp[i] += dp[i-2];
        }
    }

    return dp[n];
}
