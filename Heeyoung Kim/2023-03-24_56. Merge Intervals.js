var merge = function(intervals) {
    if(!intervals.length) return intervals;
    //Intervals is empty | return intervals
    
    intervals.sort(function(a,b) { return a[0] - b[0]});
    //Sorting Array
    
    const res = [intervals[0]]; //return Stack 
    
    for(let i =0; i<intervals.length; i++){
        const currentInterval = intervals[i]; 
        const lastInterval = res[res.length-1];
        
        if(currentInterval[0] <= lastInterval[1]) {
            lastInterval[1] = Math.max(currentInterval[1], lastInterval[1]);
        }else {
            res.push(currentInterval);
        }
    }
    
    
    return res;
    
};