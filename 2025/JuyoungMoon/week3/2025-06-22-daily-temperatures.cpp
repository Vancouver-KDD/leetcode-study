// Author: Juyoung Moon

// KDD LeetCode Study Week 3: Stack.
// https://github.com/juyomo/leetcode-study

// LeetCode #739.
// https://leetcode.com/problems/daily-temperatures/

// SOLN #1. O(n^2)
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        for (int i = 0; i < temperatures.size(); i++) {
            for (int j = i + 1; j < temperatures.size(); j++) {
                if (temperatures[j] > temperatures[i]) {
                    res[i] = j - i;
                    break;
                }
            }
        }
        return res;
    }
};
