// Author: Juyoung Moon

// KDD LeetCode Study Week 11: DP 2
// https://github.com/juyomo/leetcode-study

// LeetCode #5.
// https://leetcode.com/problems/longest-palindromic-substring/

class Solution {
public:
    string longestPalindrome(string s) {
        string currMaxStr = s.substr(0, 1);
        int currMax = 1;

        // iterate through each char in the string
        // this char will be the "pivot"
        for (int i = 0; i < s.size(); i++) {
            int j = 1; // distance from pivot char
            while (i-j >= 0 && i+j < s.size()) {
                if (s[i-j] == s[i+j]) {
                    j++;
                } else {
                    break;
                }
            }
            j--;

            // max substr 
            int currSubstrLen = 2 * j + 1;
            if (currSubstrLen > currMax) {
                currMax = currSubstrLen;
                currMaxStr = s.substr(i-j, currSubstrLen);
            }
        }

        // check for EVEN substrs
        for (int i = 0; i < s.size() - 1; i++) {
            int j = 0; 
            while (i-j >= 0 && i+j+1 < s.size()) {
                if (s[i-j] == s[i+j+1]) {
                    j++;
                } else {
                    break;
                }
            }
            j--;

            int currSubstrLen = 2 * (j + 1);
            if (((j > 0) || (j == 0 && s[i-j] == s[i+j+1])) && currSubstrLen > currMax) {
                currMax = currSubstrLen;
                currMaxStr = s.substr(i-j, currSubstrLen);
            }
        }
        return currMaxStr;
    }
};
