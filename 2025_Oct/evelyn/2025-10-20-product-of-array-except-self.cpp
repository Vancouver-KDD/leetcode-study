class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n, 1);

        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i-1] * nums[i-1];
        }

        int right = 1;

        for (int j = n-1; j >= 0; j--) {
            prefix[j] *= right;
            right *= nums[j];
        }

        return prefix;
    }
};