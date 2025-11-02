class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size()==0) return 0;

        unordered_set<char> hashmap;
        int maxLen = 1;
        int left = 0;

        for (int i = 0; i < s.size(); i++) {
            while(hashmap.count(s[i])) {
                hashmap.erase(s[left]);
                left++;
            }
            hashmap.insert(s[i]);
            maxLen = max(maxLen, i-left+1);
            
        }

        return maxLen;
    }
};