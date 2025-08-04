// Author: Juyoung Moon

// KDD LeetCode Study Week 7: Backtracking
// https://github.com/juyomo/leetcode-study

// LeetCode #39.
// https://leetcode.com/problems/combination-sum/

class Solution {
public:
    void backtrack(const vector<int>& originalArr,
                   int currIndex,
                   int remaining, 
                   vector<int>& currChoices,
                   vector<vector<int>>& finalBucket) {
        if (remaining == 0) {
            finalBucket.push_back(currChoices);
            return;
        }

        if (remaining < 0 || currIndex >= originalArr.size()) {
            return;
        }

        int currNum = originalArr[currIndex];

        // with curr elem, increment index
        currChoices.push_back(currNum);
        backtrack(originalArr, currIndex + 1, remaining - currNum, currChoices, finalBucket);

        // with curr elem, don't increment index
        backtrack(originalArr, currIndex, remaining - currNum, currChoices, finalBucket);

        // without it
        currChoices.pop_back();
        backtrack(originalArr, currIndex + 1, remaining, currChoices, finalBucket);
    }

    vector<vector<int>> removeDuplicates(vector<vector<int>>& vec) {
        if (vec.size() == 0) {
            return {};
        }

        sort(vec.begin(), vec.end());

        vector<vector<int>> res;
        res.push_back(vec[0]);

        for (int i = 1; i < vec.size(); i++) {
            if (vec[i] != vec[i-1]) {
                res.push_back(vec[i]);
            }
        }

        return res;
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> curr;
        backtrack(candidates, 0, target, curr, result);

        result = removeDuplicates(result);
        return result;
    }
};
