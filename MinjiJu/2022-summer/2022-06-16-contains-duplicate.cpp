// using set
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        set<int> s;
        for(auto num:nums){
            if(s.find(num)!=s.end()) return true;
            s.insert(num);
        }
        return false;
    }
};

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