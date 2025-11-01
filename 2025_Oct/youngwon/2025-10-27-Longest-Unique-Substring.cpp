class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxCount; 
        unordered_set<char> uniqueChars;
        for (char c : s) {
            uniqueChars.insert(c);
        }
        maxCount = uniqueChars.size();
        
        for (int i = 0; i <= maxCount; i++) {
            if (hasUniqueSubstring(s, i)) {
                continue; 
            } else {
                return i - 1;
            }
        }
        return maxCount; 
    }

    bool hasUniqueSubstring(const string &s, int x) {
        for (int i = 0; i + x <= s.size(); i++) { 
            unordered_set<char> seen;
            bool unique = true;

            for (int j = i; j < i + x; j++) {
                if (seen.count(s[j])) {
                    unique = false;
                    break;
                }
                seen.insert(s[j]);
            }

            if (unique) return true;
        }
        return false;
    }
};
