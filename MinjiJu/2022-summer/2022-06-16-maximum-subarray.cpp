class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int max_curr = nums[0];
        int max_prev = nums[0];
        
        for(int i=1; i<nums.size(); i++){
            max_prev = max(max_prev+nums[i], nums[i]);
            max_curr = max(max_curr, max_prev);
        }
        return max_curr;
    }
};