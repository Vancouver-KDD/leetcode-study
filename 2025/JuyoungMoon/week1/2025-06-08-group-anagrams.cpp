// Author: Juyoung Moon
// Solved on Wed, June 4, 2025 (KST).

// KDD LeetCode Study Week 1: Array & Hashing
// https://github.com/juyomo/leetcode-study

// https://leetcode.com/problems/group-anagrams/

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, int> strToIdx;
        vector<vector<string>> res;
        for (string s : strs) {
            string original = s;
            sort(s.begin(), s.end()); 
            if (strToIdx.find(s) != strToIdx.end()) {
                res[strToIdx[s]].push_back(original);
            } else {
                // Haven't seen this one before!
                vector<string> newVec = { original };
                strToIdx[s] = res.size();
                res.push_back(newVec);
            }
        }
        return res;
    }
};
