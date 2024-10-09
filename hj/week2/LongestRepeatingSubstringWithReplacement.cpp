class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> um;
        int mc = 0;
        int ml = 0;
        int l = 0;

        for (int r = 0; r < s.size(); r++) {
            um[s[r]]++;
            mc = max(mc, um[s[r]]);

            if (r - l + 1 - mc > k) {
                um[s[l]]--;
                l++;
            }

            ml = max(ml, r - l + 1);
        }

        return ml;
    }
};
