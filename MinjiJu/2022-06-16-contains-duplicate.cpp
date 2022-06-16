class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        sort(nums.begin(),nums.end());
        for(int i=0; i<nums.size()-1; i++){
            if(nums.at(i)==nums.at(i+1)){
                return true;
            }
        }
        return false;
    }
};