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