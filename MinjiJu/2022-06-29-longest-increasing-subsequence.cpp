class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
        if(nums.size()==0) return 0;
        
        vector<int> res;
        res.push_back(nums[0]);
        
        for(int i=1; i<nums.size(); i++){
            if(nums[i] > res.back()){
                res.push_back(nums[i]);
            }
            else{
                int j = lower_bound(res.begin(),res.end(),nums[i]) - res.begin();
                res[j] = nums[i];
            }
        }
        return res.size();
    }
};