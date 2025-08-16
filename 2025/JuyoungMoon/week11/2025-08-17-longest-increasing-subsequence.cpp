// Author: Juyoung Moon

// KDD LeetCode Study Week 11: DP 2
// https://github.com/juyomo/leetcode-study

// LeetCode #300.
// https://leetcode.com/problems/longest-increasing-subsequence/

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> dp(nums.size(), 1);
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
        }
        int max = 1;
        for (int i = 0; i < dp.size(); i++) {
            if (dp[i] > max) {
                max = dp[i];
            }
        }
        return max;
    }
};
