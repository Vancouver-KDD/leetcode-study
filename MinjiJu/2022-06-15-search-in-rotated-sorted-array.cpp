class Solution {
public:
    int search(vector<int>& nums, int target) {
        
        int res = 0;

        // find index of target within given array
        auto it = find(nums.begin(),nums.end(),target);
        
        // check if target found 
        int res = (it!=nums.end()) ? it-nums.begin() : -1; 
        /*
        if(it!=nums.end()){
            res = it - nums.begin();
        } else {
            res = -1;
        }
        */
        return res;
    }
};