// Author: Juyoung Moon
// Solved on/before Wed, June 4, 2025 (KST).
// Apparently I did this on Jan 30. Yay! Free brownie points :D

// KDD LeetCode Study Week 2: Two Pointer & Sliding Window.
// https://github.com/juyomo/leetcode-study

// LeetCode #125.
// https://leetcode.com/problems/valid-palindrome/

#include <iostream>
#include <string>
#include <algorithm> // for transform and remove_if
#include <cctype>   // for tolower and isalnum

class Solution {
public:
    bool isPalindrome(string s) {
        int start = 0;
        int end = s.size() - 1;
        while (start <= end) {
            if (!isalnum(s[start])) {
                start++; 
                continue;
            }
            if (!isalnum(s[end])) {
                end--;
                continue;
            }
            if (tolower(s[start]) != tolower(s[end])) {
                return false;
            } else {
                start++;
                end--;
            }
        }
        return true;
    }
};
