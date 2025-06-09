#include <iostream>
#include <vector>
#include <unordered_map>
//https://leetcode.com/problems/two-sum/
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        int complement;
        vector<int> output;

        for (int i = 0; i < nums.size(); i++) {
            m.insert({nums[i], i});
        }

        for (int j = 0; j < nums.size(); j++) {
            complement = target - nums[j];
            if (m.count(complement) && j != m[complement]) {
                output.push_back(j);
                output.push_back(m.find(complement)->second);
                break;
            }
        }

        return output;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;

    vector<int> result = sol.twoSum(nums, target);

    if (!result.empty()) {
        cout << "Indices: " << result[0] << ", " << result[1] << endl;
    } else {
        cout << "No two sum solution found." << endl;
    }

    return 0;
}
