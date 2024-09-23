class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> um;

        for (int i = 0; i < nums.size(); i++) {
            int gap = target - nums[i];
            if (um.find(gap) != um.end()) {
                return i < um[gap] ?
                    vector<int>{i, um[gap]} : vector<int>{um[gap], i};
            }
            um[nums[i]] = i;
        }
        return {};
    }
};
