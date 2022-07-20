class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
        vector<vector<int>> res;
        if(intervals.size()==0) return res;
        
        sort(intervals.begin(), intervals.end());
        res.push_back(intervals[0]);
        
        int j=0;
        for(int i=0; i<intervals.size(); i++){
            if(res[j][1] >= intervals[i][0]) res[j][1] = max(res[j][1], intervals[i][1]);
            else{
                res.push_back(intervals[i]);
                j++;
            }
        }
        return res;
    }
};