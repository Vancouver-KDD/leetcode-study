// Author: Juyoung Moon
// Solved on/before Wed, June 4, 2025 (KST).
// Apparently I did this on Feb 09. Yay! Free brownie points :D

// KDD LeetCode Study Week 2: Two Pointer & Sliding Window.
// https://github.com/juyomo/leetcode-study

// LeetCode #3.
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // if (s.size() < 2) return s.size();

        unordered_map<char, int> lastIndex;
        int startOfCurrString = 0;

        int maxLength = 0;
        // |abc|abcdbb
        // a|bca|bcdbb <- update startOfCurrString
        // ab|cab|cdbb
        // abc|abc|dbb
        // abc|ab cd|bb
        // abc ab|cd b|b <- important logic2 -- need to have stored length of prev "abcd" AND index of a
        
        for (int i = 0; i < s.length(); i++) {
            char currChar = s[i];
            if (lastIndex.find(currChar) == lastIndex.end() || lastIndex[currChar] == -1) {
                // it's a non repeating character, we're good!
                lastIndex[currChar] = i;
            } else {
                // need to also update lastIndex[c] of all other chars we are removing
                for (int j = startOfCurrString; j < lastIndex[currChar]; j++) {
                    lastIndex[s[j]] = -1;
                }

                int tmp = i - startOfCurrString;
                if (tmp > maxLength) {
                    maxLength = tmp;
                }
                startOfCurrString = lastIndex[currChar] + 1;
                lastIndex[currChar] = i;
            }
        }
        int tmp = s.size() - startOfCurrString;
        if (tmp > maxLength) {
            maxLength = tmp;
        }
        return maxLength;
    }
};
