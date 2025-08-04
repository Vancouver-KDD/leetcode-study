// Author: Juyoung Moon
// KDD LeetCode Study Week 2: Two Pointer & Sliding Window.
// https://github.com/juyomo/leetcode-study

// LeetCode #424.
// https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> frequencies;

        int maxLen = 0;
        int maxFreq = 0;
        int i = 0;

        for (int j = 0; j < s.size(); j++) {
            frequencies[s[j]]++;
            maxFreq = max(maxFreq, frequencies[s[j]]);

            if ((j - i + 1) - maxFreq > k) {
                frequencies[s[i]]--;
                i++;
            }

            maxLen = max(maxLen, j - i + 1);
        }

        return maxLen;
    }
};