class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> output;
        unordered_map<string, vector<string>> um;

        for (string &str : strs) {
            string key = str;
            sort(key.begin(), key.end());
            um[key].push_back(str);
        }

        for (auto &val : um) {
            output.push_back(val.second);
        }

        return output;
    }
};
