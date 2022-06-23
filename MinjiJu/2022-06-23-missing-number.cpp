// using Gauss' Formula
// sum{0, 1, ..., n} = n(n+1)/2
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int sum_exp =  nums.size()*(nums.size()+1)/2;
        int sum_act = 0;
        
        for (int i=0; i<nums.size(); i++) {
            sum_act+=nums[i];
        }
        return sum_exp - sum_act;
    }
};

// naive approach
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size()+1;
        for(int i=0; i<n; i++){
            auto it = find(nums.begin(), nums.end(), i);
            if(it!=nums.end()) continue;
            else{
                return i;
            }
        }
        return 0;
    }
};