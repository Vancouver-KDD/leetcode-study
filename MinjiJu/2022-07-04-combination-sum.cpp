class Solution {
public:
    
    vector<vector<int>> res;    // 2d vector for storing result
    vector<int> cur;            // current vector
    
    // backtracking
    void combination(vector<int>& candidates, int target, int index){
        
        // combination found - add current vector to result vector
        if(target==0){
            res.push_back(cur);
            return;
        }
        
        // combination no longer possible
        if(index==candidates.size() || target<0) return;
        
        // include index-th element and recurse using decreased sum
        cur.push_back(candidates[index]);
        combination(candidates, target-candidates[index], index);
        
        // backtrack and move to next index
        cur.pop_back();
        combination(candidates, target, index+1);
    }
    
    // solution
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        combination(candidates, target, 0);
        return res;
    }
};