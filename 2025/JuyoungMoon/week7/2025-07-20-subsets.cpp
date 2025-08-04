// Author: Juyoung Moon

// KDD LeetCode Study Week 7: Backtracking
// https://github.com/juyomo/leetcode-study

// LeetCode #78.
// https://leetcode.com/problems/subsets/

class Solution {

private:

    void subsetRecur(int nthNum,
                     const vector<int>& originalList,
                     vector<vector<int>>& listOfSubsets,
                     vector<int>& current) {
        // we are at a leaf node
        if (nthNum == originalList.size()) {
            listOfSubsets.push_back(current);
            return;
        }

        subsetRecur(nthNum + 1, originalList, listOfSubsets, current);
        current.push_back(originalList[nthNum]);
        subsetRecur(nthNum + 1, originalList, listOfSubsets, current);
        current.pop_back();
    }

public:

    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> curr;
        vector<vector<int>> listOfSubsets;
        subsetRecur(0, nums, listOfSubsets, curr);
        return listOfSubsets;
    }

};
