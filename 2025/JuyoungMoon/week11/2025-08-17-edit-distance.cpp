// Author: Juyoung Moon

// KDD LeetCode Study Week 11: DP 2
// https://github.com/juyomo/leetcode-study

// LeetCode #72.
// https://leetcode.com/problems/edit-distance/

class Solution {
public:
    int min(int a, int b, int c) {
        int res = a;
        if (b < res) {
            res = b;
        }
        if (c < res) {
            res = c;
        }
        return res;
    }

    int minDistance(string a, string b) {
        int kMax = 10000000000;
        vector<vector<int>> dp(a.size() + 1, vector<int>(b.size() + 1, kMax));

        for (int i = 0; i < dp.size(); i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j < dp[0].size(); j++) {
            dp[0][j] = j;
        }

        for (int r = 1; r < dp.size(); r++) {
            char aChar = a[r - 1];
            for (int c = 1; c < dp[0].size(); c++) {
                char bChar = b[c - 1];
                if (aChar == bChar) {
                    dp[r][c] = dp[r-1][c-1];
                } else {
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]);
                }
            }
        }

        return dp[dp.size() - 1][dp[0].size() - 1];
    }
};
