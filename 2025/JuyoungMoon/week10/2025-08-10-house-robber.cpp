// Author: Juyoung Moon

// KDD LeetCode Study Week 10: DP
// https://github.com/juyomo/leetcode-study

// LeetCode #198.
// https://leetcode.com/problems/house-robber/

class Solution {
public:
    int findMax(int a, int b) {
        return a > b ? a : b;
    }
    int rob(vector<int>& nums) {
        int size = nums.size();
        if (size == 0) {
            return 0;
        } else if (size == 1) {
            return nums[0];
        }

        vector<int> max(size);
        max[0] = nums[0];
        max[1] = findMax(nums[0], nums[1]);

        for(int i = 2; i < size; i++) {
            max[i] = findMax(nums[i] + max[i-2], max[i-1]);
        }

        return max[size-1];
    }
};
