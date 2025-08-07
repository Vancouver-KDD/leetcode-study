// Author: Juyoung Moon

// KDD LeetCode Study Week 9: Greedy
// https://github.com/juyomo/leetcode-study

// LeetCode #134.
// https://leetcode.com/problems/gas-station/

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int len = gas.size();
        vector<int> total(len);

        int gasSum = 0;
        int costSum = 0; 
        for (int i = 0; i < len; i++) {
            gasSum += gas[i];
            costSum += cost[i];
            total[i] = gas[i] - cost[i];
        }
        if (gasSum < costSum) {
            return -1;
        }

        int sum = 0;
        int startIndex = 0;
        for (int j = 0; j < len; j++) {
            sum += total[j];
            if (sum < 0) {
                sum = 0;
                startIndex = j+1;
            }
        }
        return startIndex;
    }
};
