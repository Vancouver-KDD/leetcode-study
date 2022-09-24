class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.size() != t.size()) {
            return false;
        }
        
        map<char, int> count;
        for (char c : s) {
            count[c]++;
        }
        
        for (char c : t) {
            count[c]--;
        }
        
        for (auto it : count) {
            if (it.second != 0) {
                return false;
            }
        }
        return true;
    }
};