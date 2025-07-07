// Author: Juyoung Moon

// KDD LeetCode Study Week 4: Binary Search.
// https://github.com/juyomo/leetcode-study

// LeetCode #704.
// https://leetcode.com/problems/binary-search/

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int size = nums.size();
        int start = 0;
        int end = size - 1;
        while (start >= 0 && start < size && end >= 0 && end < size && start <= end) {
            int idx = (end+start)/2;
            int curr = nums[idx];
            if (curr == target) {
                return idx;
            } else if (curr < target) {
                start = idx + 1;
            } else {
                end = idx - 1;
            }
        }
        return -1;
    }
};
