class Solution {
public:
    string longestPalindrome(string s) {
        int slen = s.size();
        if (slen == 0) return "";

        vector<vector<int>> dp_table(slen, vector<int>(slen, 0));

        for (int i = 0; i < slen; i++) {
            dp_table[i][i] = 1;
        }

        int max_length = 1;
        int start_idx = 0;

        for (int i = 0; i < slen - 1; i++) {
            if (s[i] == s[i + 1]) {
                dp_table[i][i + 1] = 2;
                start_idx = i;
                max_length = 2;
            }
        }

        for (int length = 3; length <= slen; length++) {
            for (int i = 0; i < slen - length + 1; i++) {
                int j = i + length - 1;

                if (s[i] == s[j] && dp_table[i + 1][j - 1] > 0) {
                    dp_table[i][j] = dp_table[i + 1][j - 1] + 2;

                    if (dp_table[i][j] > max_length) {
                        max_length = dp_table[i][j];
                        start_idx = i;
                    }
                }
            }
        }

        return s.substr(start_idx, max_length);
    }
};