// Given a string s, return the number of palindromic substrings in it.

// A string is a palindrome when it reads the same backward as forward.

// A substring is a contiguous sequence of characters within the string.

// Input: s = "abc"
// Output: 3
// Explanation: Three palindromic strings: "a", "b", "c".

public int countSubstrings(String s) {
    int n = s.length();
    int count = 0;
    
    for (int center = 0; center < 2 * n - 1; center++) {
        int left = center / 2;
        int right = left + center % 2;
        
        while (left >= 0 && right < n && s.charAt(left) == s.charAt(right)) {
            count++;
            left--;
            right++;
        }
    }
    return count;
}