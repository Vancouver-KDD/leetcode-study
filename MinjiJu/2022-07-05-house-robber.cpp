// space-optimized dp
class Solution {
public:
    int rob(vector<int>& nums) {
        
        int prev2=0, prev=0, cur=0;
        
        for(auto i:nums){
            cur = max(prev, i+prev2);
            prev2 = prev;
            prev = cur;
        }
        return cur;
    }
};


// dp - tabulation
class Solution {
public:
    int rob(vector<int>& nums) {
        
        vector<int> dp(nums);
        
        if(nums.size()==1) return nums[0];
        dp[1] = max(nums[0],nums[1]);
        
        for(int i=2; i<nums.size(); i++){
            dp[i] = max(dp[i-1], nums[i]+dp[i-2]);
        }
        
        return dp[nums.size()-1];
    }
};

// dp - memoization
class Solution {
public:
    
    int res;
    
    int rob(vector<int>& nums, vector<int>& dp, int i){
        if(i>=nums.size()) return 0;
        if(dp[i]!=-1) return dp[i];
        
        dp[i] = max(rob(nums,dp,i+1), nums[i]+rob(nums,dp,i+2));
        return dp[i];
    }
    
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        res = rob(nums, dp, 0);
        return res;
    }
};
