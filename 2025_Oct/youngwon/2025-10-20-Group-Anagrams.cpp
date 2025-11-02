class Solution {
public:
      vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<string> sorted_strs = strs;  
        unordered_map<string, vector<int>> anagram_groups;

       
        for (int i = 0; i < sorted_strs.size(); ++i) {
            string sorted = sorted_strs[i];
            sort(sorted.begin(), sorted.end());
            anagram_groups[sorted].push_back(i);  
        }

        vector<vector<string>> result;
        for (const auto& [key, indices] : anagram_groups) {
            vector<string> group;
            for (int idx : indices) {
                group.push_back(strs[idx]);
            }
            result.push_back(move(group));
        }

        return result;