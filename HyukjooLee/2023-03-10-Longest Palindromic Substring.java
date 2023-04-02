// Given a string s, return the longest palindromic substring in s.

// Input: s = "babad"
// Output: "bab"
// Explanation: "aba" is also a valid answer.

// Input: s = "cbbd"
// Output: "bb"

// 입력 string 의 가능한 모든 substring 들을 반복하면서 palindromic substring 인지 확인
// substring 의 중간에서 시작해서 양쪽 끝으로 바깥쪽으로 이동하는 two pointers 을 이용 할 수 있음

// using two pointers starting from the middle of the substring and moving outwards both ends
// time complexity is O(N^3) 
// possible substrings of the string O(N^2) * O(N); using the two-pointer technique
// space complexity is O(1); extra space to store the indices of the substring found so far
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
