// take 2
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int res=nums[0], left=0, right=0;
        
        for(int i=0; i<n; i++){
            left = (left ? left : 1)*nums[i];           // product from left
            right = (right ? right : 1)*nums[n-1-i];    // product from right
            res = max(res, max(left,right));            // compare and update max
        }
        return res;
    }
};

// init brute force approach
// maximum time limit exceeded

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
        int prod = nums.at(0);
        
        for(int i=0; i<nums.size(); i++){
            int temp=1;
            for(int j=i; j<nums.size(); j++){
                
                temp*=nums.at(j);
                prod = max(prod,temp);
            }
        }
        return prod;
    }
};