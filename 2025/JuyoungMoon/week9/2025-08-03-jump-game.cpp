// Author: Juyoung Moon

// KDD LeetCode Study Week 9: Greedy
// https://github.com/juyomo/leetcode-study

// LeetCode #55.
// https://leetcode.com/problems/jump-game/

class Solution {
public:
    bool canJump(vector<int>& nums) {
        int goal = nums.size() - 1;
        int start = goal - 1;

        while (start >= 0) {
            if (nums[start] >= goal - start) {
                goal = start;
                start = goal - 1;
            } else {
                start--;
            }
        }
        return goal == 0;
    }
};
