class Solution {
public:
    bool canJump(vector<int>& nums) {
        
        int jump = nums[0];
        
        //already at last index
        if(nums.size()==1) return true;
        
        // unable to jump to any other index
        if(jump==0) return false;
        
        
        for(int i=1; i<nums.size(); i++){
            
            // last index reached
            if(i==nums.size()-1) return true;
            
            jump = max(jump-1, nums[i]);
            
            // stuck at 0
            if(jump==0) return false;
        }
        return false;
    }
};