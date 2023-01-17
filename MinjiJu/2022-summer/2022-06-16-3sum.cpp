class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        
        if(nums.size()<3) return res;
        
        for(int i=0; i<nums.size()-1; i++){
            
            if(i>0 && nums[i]==nums[i-1]) continue;
            
            int left=i+1, right=nums.size()-1;
            
            while(left<right){
                int sum = nums[i] + nums[left] + nums[right];
                if(sum<0) left++;
                else if(sum>0) right--;
                else{   // triplet found
                    res.push_back({nums[i],nums[left],nums[right]});
                    
                    while(left+1<right && nums[left]==nums[left+1]) left++;
                    while(left<right-1 && nums[right]==nums[right-1]) right--;
                    
                    left++;
                    right--;
                }
            }
        }
        return res;
    }
};