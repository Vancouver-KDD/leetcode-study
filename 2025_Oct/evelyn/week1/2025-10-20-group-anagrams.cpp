class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;

        for (string str: strs) {
            string key = str;
            sort(key.begin(), key.end());
            hashmap[key].push_back(str);
        }

        vector<vector<string>> ans;
        ans.reserve(hashmap.size());

        for (auto& kv: hashmap) {
            ans.push_back(kv.second);
        }

        return ans;
        
    }
};

class Solution {
public:
    string genVec(const string& s) {
        vector<int> ans(26, 0);
        for (char c: s) ans[c-'a']++;

        string key;
        for (int i = 0; i < 26; i++) {
            key += to_string(ans[i]) + '#';
        }

        return key;
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;
        unordered_map<string, vector<string>> hash_map;

        for (string str: strs) {
            string key = genVec(str);
            hash_map[key].push_back(str);
        }

        for (auto& kv: hash_map) {
            ans.push_back(kv.second);
        }

        return ans;
    }
};