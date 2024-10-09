class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n1 = s1.size();
        int n2 = s2.size();

        unordered_map<char, int> um1;
        unordered_map<char, int> um2;

        for (auto &c : s1) um1[c]++;
        for (int i = 0; i < n1; i++) {
            um2[s2[i]]++;
        }

        if (um1 == um2) return true;

        for (int i = n1; i < n2; i++) {
            um2[s2[i]]++;
            um2[s2[i - n1]]--;
            if (um2[s2[i - n1]] == 0)
                um2.erase(s2[i - n1]);

            if (um1 == um2) return true;
        }

        return false;
    }
};
