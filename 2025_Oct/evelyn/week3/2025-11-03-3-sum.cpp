class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] > 0) break;

            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int lp = i + 1;
            int rp = nums.size() - 1;

            while (lp < rp) {
                int sum = nums[i] + nums[lp] + nums[rp];

                if (sum == 0) {
                    result.push_back({nums[i], nums[lp], nums[rp]});

                    while (lp < rp && nums[lp] == nums[lp + 1]) ++lp;
                    while (lp < rp && nums[rp] == nums[rp - 1]) --rp;

                    ++lp;
                    --rp;
                    
                } else if (sum < 0) {
                    ++lp;
                } else {
                    --rp;
                }
            }
        }

        return result;
    }
};
