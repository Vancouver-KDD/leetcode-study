/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    const len = intervals.length;
    if (len<2) return intervals;
    
    intervals.sort((a,b) => a[0] - b[0]);
    const res = [intervals[0]];
    let resIdx = 0;
    
    for (let i=1; i<len; i++){
        if (res[resIdx][1] >= intervals[resIdx][i]){
            res[resIdx][1] = Math.max(intervals[i][1], res[resIdx][1]);
        }else{
            res.push(intervals[i]);
            resIdx++;
        }
    }
    return res;
};
