class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());  
        vector<vector<int>> output;
        vector<int> subset;
        backtrack(candidates, target, 0, subset, output);
        return output;
    }

    void backtrack(vector<int>& candidates, int target, int idx, vector<int>& subset, vector<vector<int>>& output) {
        if (target == 0) {
            output.push_back(subset);  
            return;
        }

        for (int i = idx; i < candidates.size(); i++) {
            if (i > idx && candidates[i] == candidates[i - 1]) continue; 
            if (candidates[i] > target) break; 

            subset.push_back(candidates[i]);
            backtrack(candidates, target - candidates[i], i + 1, subset, output);  
            subset.pop_back(); 
        }
    }
};