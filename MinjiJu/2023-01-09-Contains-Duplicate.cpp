//---------------------------------------
// Using vector and sort
//---------------------------------------
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        bool res = false;
        sort(nums.begin(), nums.end());

        for(int i=0; i<nums.size()-1; i++){
            if(nums[i]==nums[i+1]) res = true;
        }
        return res;
    }
};

//---------------------------------------
// Using set
//---------------------------------------
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        set<int> s;
        for(int i=0; i<nums.size(); i++){
            s.insert(nums[i]);
        }
        if(s.size()<nums.size()) return true;
        else return false;
    }
};

// condensed version of above
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        set<int> s(nums.begin(), nums.end());

        return s.size()<nums.size();
    }
};

// even more condensed version of above
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        return set<int>(nums.begin(), nums.end()).size()<nums.size();
    }
};

//---------------------------------------
// Using unordered_map
//---------------------------------------
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // key: (int) element
        // value: (bool) exists/doesn't exist

        unordered_map<int,bool> mp; // create empty map
        
        for(auto num:nums){
            if(mp.find(num)!=mp.end()) return true; // element exists
            mp[num] = true; // add element to map
        }
        return false;   
        
    }
};

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        // key: (int) element
        // value: (int) frequency

        unordered_map<int,int> mp;
        for(auto num : nums){
            mp[num]++;
        }
        for(auto e : mp){
            if(e.second >= 2) return true;  // element appears at least twice
        }
        return false;
    }
};

// same stuff as above
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        // map frequency of element
        unordered_map<int,int> mp;
        for(int i=0; i<nums.size(); i++){
            mp[nums[i]]++;
        }

        // check if any value has 1+ frequency
        for(auto &x : mp){
            if(x.second > 1) return true;
        }
        return false;
    }
};