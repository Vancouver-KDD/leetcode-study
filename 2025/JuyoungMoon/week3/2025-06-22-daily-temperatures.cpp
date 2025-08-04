// Author: Juyoung Moon
// Solved on: Mon, June 23, 2025 (KST).

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

// SOLN #2. O(n)
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(), 0);
        stack<int> indices;
        for (int i = 0; i < temperatures.size(); i++) {
            while (!indices.empty() && temperatures[indices.top()] < temperatures[i]) {
                res[indices.top()] = i - indices.top();
                indices.pop();
            }
            indices.push(i);
        }
        return res;
    }
};
