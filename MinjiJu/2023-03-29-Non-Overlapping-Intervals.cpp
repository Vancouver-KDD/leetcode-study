class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        
        // sort intervals based on start val
        sort(intervals.begin(), intervals.end());

        // keep track of count (of erased interval) and the previous end val
        int count=0, end=intervals[0][1];
        
        for(int i=1; i<intervals.size(); i++){
            
            // if interval's start val is less than prev end val
            // (i.e. intervals overlap)
            if(intervals[i][0]<end){
                
                // let prev end val be the lesser of the two
                // (i.e. remove interval with higher end val)
                end = min(end, intervals[i][1]);
                
                // increment count of "erased interval"
                count++;
            }
            
            // if the intervals do not overlap
            else{
            
                // replace prev end val with current end val
                end = intervals[i][1];
            }
        }
        return count;
    }
};



class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        
        sort(intervals.begin(), intervals.end());

        int count=0, end=intervals[0][1];
        
        for(int i=1; i<intervals.size(); i++){
            if(intervals[i][0]<end){
                end = min(end, intervals[i][1]);
                count++;
            }
            else{
                end = intervals[i][1];
            }
        }
        return count;
    }
};