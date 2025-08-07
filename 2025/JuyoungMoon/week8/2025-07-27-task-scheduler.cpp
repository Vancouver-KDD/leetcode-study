// Author: Juyoung Moon

// KDD LeetCode Study Week 8: Heap / Priority Queue
// https://github.com/juyomo/leetcode-study

// LeetCode #621.
// https://leetcode.com/problems/task-scheduler/

class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        unordered_map<char, int> counts;
        for (char c : tasks) {
            counts[c]++;
        }

        int maxFreq = 0;
        int total = 0;
        for (const auto& p : counts) {
            if (p.second > maxFreq) {
                maxFreq = p.second;
            }
            total += p.second;
        }

        int howManyAtMaxFreq = 0;
        for (const auto& p : counts) {
            if (p.second == maxFreq) {
                howManyAtMaxFreq++;
            }
        }

        int width = n + 1;
        int res = width * (maxFreq - 1) + howManyAtMaxFreq;
        
        return max(total, res);
    }
};
