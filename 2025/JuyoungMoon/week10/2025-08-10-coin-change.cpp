// Author: Juyoung Moon

// KDD LeetCode Study Week 10: DP
// https://github.com/juyomo/leetcode-study

// LeetCode #322.
// https://leetcode.com/problems/coin-change/

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int kMax = 100000;
        vector<int> dp(amount + 1, kMax);

        dp[0] = 0;
        for (int i = 0; i < coins.size(); i++) {
            if (coins[i] < dp.size()) {
                dp[coins[i]] = 1;
            }
        }
        for (int currAmt = 1; currAmt <= amount; currAmt++) {
            for (int j = 0; j < coins.size(); j++) {
                int coinAmt = coins[j];
                int prev = currAmt - coinAmt;
                if (currAmt - coinAmt >= 0 && (dp[prev] + 1 < dp[currAmt])) {
                    dp[currAmt] = dp[prev] + 1;
                }
            }
        }

        return (dp[amount] == kMax) ? -1 : dp[amount];
    }
};
