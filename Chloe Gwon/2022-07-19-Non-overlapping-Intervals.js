/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    intervals.sort((a, b) => a[0] - b[0])
    const n = intervals.length
    let count = 0

	//'po' as 'previous low' and 'pi' as 'previous high'
    let [po, pi] = intervals[0]
	
    for(let i = 1; i < n; i++){
		//'co' as 'current low' and 'ci' as 'current high'
        const [co, ci] = intervals[i]

        if(pi > co && pi > ci) {
            count++
            po = co
            pi = ci
        }
        else if(pi > co) count++
        else {
            po = co
            pi = ci
        }
    }
    return count
};

