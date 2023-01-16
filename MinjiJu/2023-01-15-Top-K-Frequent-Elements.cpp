class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        vector<int> res;
        
        unordered_map<int,int> m;
        for(int i=0; i<nums.size(); i++){
            m[nums[i]]++;
        }
        
        set<pair<int,int>> s;
        for(auto it=m.begin(); it!=m.end(); it++){
            s.insert({it->second, it->first});
        }
        
        auto it = s.end();
        it--;
        
        for(int i=1; i<=k; i++){
            res.push_back(it->second);
            it--;
        }
        return res;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        vector<int> res;        
        if(nums.empty()) return res;
        
        unordered_map<int, int> keys;
        for(auto n:nums) keys[n]++;
        
        vector<vector<int>> buckets(nums.size()+1);
        
        for(auto& pair:keys) buckets[pair.second].push_back(pair.first);
        
        for(int i=nums.size(); i; --i){
            for(int j=0; j<buckets[i].size(); ++j){
                res.push_back(buckets[i][j]);
                if(res.size()==k) return res;
            }
        }
        return res;
    }
};