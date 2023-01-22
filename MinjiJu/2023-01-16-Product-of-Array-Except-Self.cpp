class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        // product of elements to the left of the i-th element
        vector<int> left(nums.size());
        left[0] = 1;
        for(int i=1; i<nums.size(); i++){
            left[i] = left[i-1]*nums[i-1];
        }
        
        // product of elements to the right of the i-th element
        vector<int> right(nums.size());
        right[nums.size()-1] = 1;
        for(int i=nums.size()-2; i>=0; i--){
            right[i] = right[i+1]*nums[i+1];
        }
        
        // dot product of left and right
        vector<int> res(nums.size());
        for(int i=0; i<nums.size(); i++){
            res[i] = left[i]*right[i];
        }
        
        return res;
    }
};