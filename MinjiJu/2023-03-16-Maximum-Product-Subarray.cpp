class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int res=nums[0], left=0, right=0;
        
        for(int i=0; i<n; i++){
            left = (left ? left : 1)*nums[i];
            right = (right ? right : 1)*nums[n-1-i];
            res = max(res, max(left,right));
        }
        return res;
    }
};