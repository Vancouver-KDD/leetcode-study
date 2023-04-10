class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        // given expected elements in nums = n
        // nums = {0,1,2,...,n-1} => missing val = n
        // initialize res to n
        int res = nums.size();  
        
        // xor with each index and value to find missing number
        for(int i=0; i<nums.size(); i++){
            res = res^(i^nums[i]);
        }
        return res;
    }
};