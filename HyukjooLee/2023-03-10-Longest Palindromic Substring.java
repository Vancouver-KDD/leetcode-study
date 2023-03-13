// Given a string s, return the longest  palindromic substring in s

// Input: s = "babad"
// Output: "bab"
// Explanation: "aba" is also a valid answer.

// Input: s = "cbbd"
// Output: "bb"

// 1. looping through each character in the string as the center of a potential palindrome,
// and expand around that center to check for palindromes of even and odd length
// time complexity is O(N^2) = the length of the string, 
// space complexity is O(1) as we only use a constant amount of extra space (start and end)
public String longestPalindrome(String s) {
    int n = s.length();
    if (n < 2) {
        return s;
    }
    
    int start = 0;
    int end = 0;
    
    for (int i = 0; i < n; i++) {
        // check for odd palindrome
        int len1 = expandAroundCenter(s, i, i);
        // check for even palindrome
        int len2 = expandAroundCenter(s, i, i+1);
        int len = Math.max(len1, len2);
        
        // if we found a longer palindrome, update the start and end
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    
    return s.substring(start, end+1);
}

// helper function to expand around a center character to find a palindrome
// return the length of the palindrome centered
private int expandAroundCenter(String s, int left, int right) {
    int n = s.length();
    while (left >= 0 && right < n && s.charAt(left) == s.charAt(right)) {
        left--;
        right++;
    }
    return right - left - 1;
}
