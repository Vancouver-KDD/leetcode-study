lass Solution {
public:
    
    vector<vector<int>> res;
    vector<int> cur;
    
    void combination(vector<int>& candidates, int target, int index){
        if(target==0){
            res.push_back(cur);
            return;
        }
        if(index==candidates.size() || target<0) return;
        
        cur.push_back(candidates[index]);
        combination(candidates, target-candidates[index], index);
        cur.pop_back();
        combination(candidates, target, index+1);
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        combination(candidates, target, 0);
        return res;
    }
};

/*
vector<vector<int>>result;
vector<int>current;

void function(vector<int>& candidates,int target,int index)
{
    if(target==0){
        result.push_back(current);
        return;
    }
    
    if(index==candidates.size() || target<0)return;
    
    current.push_back(candidates[index]);
    function(candidates,target-candidates[index],index);
    current.pop_back();
    function(candidates,target,index+1);      
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    function(candidates,target,0);
    return result;
}
*/