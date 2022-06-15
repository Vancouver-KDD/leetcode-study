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