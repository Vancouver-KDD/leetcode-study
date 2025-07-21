// Author: Juyoung Moon

// KDD LeetCode Study Week 7: Backtracking
// https://github.com/juyomo/leetcode-study

// LeetCode #46.
// https://leetcode.com/problems/permutations/

class Solution {
public:
    void backtrack(const vector<int>& originalArr,
                   vector<bool>& used,
                   vector<int>& currChoices,
                   vector<vector<int>>& finalBucket) {
        if (currChoices.size() == originalArr.size()) {
            finalBucket.push_back(currChoices);
            return;
        }

        for (int i = 0; i < used.size(); i++) {
            if (!used[i]) {
                currChoices.push_back(originalArr[i]);
                used[i] = true;
                backtrack(originalArr, used, currChoices, finalBucket);
                used[i] = false;
                currChoices.pop_back();
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<bool> used(nums.size(), false);
        vector<int> curr;
        vector<vector<int>> res;
        backtrack(nums, used, curr, res);
        return res;
    }
};
