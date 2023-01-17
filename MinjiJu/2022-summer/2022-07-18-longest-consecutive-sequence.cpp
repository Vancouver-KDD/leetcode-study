class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        // sequence does not exist
        if(nums.size()<1) return 0;
        
        // sort input array
        sort(nums.begin(), nums.end());

        // keep track of current and cumulative maximum longest consecutive sequence
        int res=1, cur=1;
        
        for(int i=1; i<nums.size(); i++){
            
            if(nums[i]!=nums[i-1]){
                if(nums[i]==nums[i-1]+1) cur++;
                else cur = 1;
            }
            res = max(res,cur);
        }
        return res;
    }
};