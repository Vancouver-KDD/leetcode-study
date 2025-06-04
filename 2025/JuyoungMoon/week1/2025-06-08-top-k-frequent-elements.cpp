// Author: Juyoung Moon
// Solved on Wed, June 4, 2025 (KST).

// KDD LeetCode Study Week 1: Array & Hashing
// https://github.com/juyomo/leetcode-study

// https://leetcode.com/problems/top-k-frequent-elements/

class Solution {
public:
    static bool compare(const vector<int>& a, const vector<int>& b) {
        // most frequent first
        return a[0] > b[0];
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Keep track of how many of each num is in array.
        unordered_map<int, int> counts;
        for (int n : nums) {
            counts[n]++;
        }

        // Put that data into a vector.
        vector<vector<int>> countAndNum(counts.size(), vector<int>(2));
        int idx = 0;
        for (const auto& p : counts) {
            int num = p.first;
            int count = p.second;
            countAndNum[idx][0] = count;
            countAndNum[idx][1] = num;
            idx++;
        }

        // Sort from most frequent to least frequent. Meh, could do better time complexity.
        sort(countAndNum.begin(), countAndNum.end(), compare);

        // Return the top k frequent.
        vector<int> res(k);
        for (int i = 0; i < k; i++) {
            res[i] = countAndNum[i][1];
        }
        return res;
    }
};