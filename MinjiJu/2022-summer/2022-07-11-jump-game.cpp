// greedy approach 2
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
            
            // take max jump possible
            // between previous jump-1 (incremented index) vs. current element
            jump = max(jump-1, nums[i]);
            
            // stuck at 0
            if(jump==0) return false;
        }
        return false;
    }
};

// greedy approach
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int dist = 0;
        for(int i=0; i<nums.size(); i++){
            if(dist<i) return false;
            dist = max(i+nums[i],dist);
        }
        return true;
    }
};
