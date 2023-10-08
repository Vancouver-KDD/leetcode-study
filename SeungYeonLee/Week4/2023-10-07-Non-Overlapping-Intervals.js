/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    let rows = intervals.length;
    let res = 0;

    // for(let i = 0; i < intervals.length; i++){
    //     for(let j = 0; j < intervals[i].length; j++){
    //         console.log(intervals[i][j] + " ");
    //     }
    //     console.log("\n");
    // }

    for (let i = 1; i < rows; i++) {
        if(intervals[i][0] < intervals[i-1][1]){
            res++;
            if(intervals[i][1]>intervals[i-1][1]){
                intervals[i] = intervals[i-1];
            }
            // intervals[i] = intervals[i-1];
        }
    }

    return res;
};