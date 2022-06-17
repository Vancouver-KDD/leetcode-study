// take 2
// product of product left of self and product right of self
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans(nums.size());
        vector<int> left(nums.size());
        vector<int> right(nums.size());
        
        // product on the left for each indices
        left[0]=1;
        for(int i=1; i<nums.size(); i++){
            left[i] = left[i-1]*nums[i-1];
        }
        // product on the right for each indices
        right[nums.size()-1]=1;
        for(int i=nums.size()-2; i>=0; i--){
            right[i]=right[i+1]*nums[i+1];
        }
        
        // product of left and right
        for(int i=0; i<nums.size(); i++){
            ans[i] = left[i]*right[i];
        }
        return ans;
    }
};

// take 1 brute force
// time limit exceeded
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer;
        int idx = 0;
        
        while(idx<nums.size()){
            int prod = 1;
            for(int i=0; i<nums.size(); i++){
                if(idx==i) continue;
                prod*=nums[i];
            }
            answer.push_back(prod);
            idx++;
        }
        return answer;
    }
};