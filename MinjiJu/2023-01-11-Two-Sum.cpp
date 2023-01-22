//---------------------------------------
// Using unordered_map
//---------------------------------------
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int,int> mp;
        vector<int> res;

        for(int i=0; i<nums.size(); i++){
            if(mp.find(target-nums[i]) != mp.end()){
                // value exists in map
                res.push_back(mp[target-nums[i]]);
                res.push_back(i);        
            }
            mp[nums[i]] = i;
        }
        return res;
    }
};

//---------------------------------------
// Using vector
//---------------------------------------
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> res;
        
        for(int i=0; i<=nums.size(); i++){
            for(int j=i+1; j<=nums.size()-1; j++){
                if(nums[i]+nums[j]==target){
                    res.push_back(i);
                    res.push_back(j);
                    return res;
                }
            }
        }
        return res;
    }
};

// same stuff as above
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        vector<int> res;    // result vector

        for(int i=0; i<nums.size()-1; i++){
            for(int j=i+1; j<nums.size(); j++){
                if(nums[i]+nums[j]==target){
                    res = {i,j};
                }
            }
        }
        return res;
    }
};