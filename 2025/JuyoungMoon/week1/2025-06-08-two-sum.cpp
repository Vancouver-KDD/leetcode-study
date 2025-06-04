// Author: Juyoung Moon
// Solved on Wed, June 4, 2025 (KST).

// KDD LeetCode Study Week 1: Array & Hashing
// https://github.com/juyomo/leetcode-study

// https://leetcode.com/problems/two-sum/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // ======= SOLUTION 1. BRUTE FORCE. O(N^2). =======
        /*
        for (int i = 0; i < nums.size(); i++) {
            int lookFor = target - nums[i];
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[j] == lookFor) {
                    return {i, j};
                }
            }
        }
        return {0, 0};
        */

        // ======= SOLUTION 2. TWO PASSES. O(N). First pass to store each index. =======
        /*
        unordered_map<int, int> numToIndex(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            numToIndex[nums[i]] = i;
        }
        for (int j = 0; j < nums.size(); j++) {
            int lookFor = target - nums[j];
            if (numToIndex.find(lookFor) != numToIndex.end() && j != numToIndex[lookFor]) {
                return {j, numToIndex[lookFor]};
            }
        }
        return {  };
        */

        // ======= SOLUTION 3. ONE PASS. O(N). =======
        unordered_map<int, int> numToIndex(nums.size());
        for (int i = 0; i < nums.size(); i++) {
            int lookFor = target - nums[i];
            if (numToIndex.find(lookFor) != numToIndex.end()) {
                return {i, numToIndex[lookFor]};
            } else {
                numToIndex[nums[i]] = i;
            }
        }
        return {  };
    }
};