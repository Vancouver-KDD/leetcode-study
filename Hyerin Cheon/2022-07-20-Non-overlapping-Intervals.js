function eraseOverlapIntervals(intervals){
  intervals.sort((a,b) => a[1] - b[1]);     // sort by earliest finish time
  let prev = intervals[0];
  let countRemove = 0;

  for(let i = 1; i < intervals.length; i++){
    const endOfPrev = prev[1];
    const startOfCurr = intervals[i][0];

    if(endOfPrev <= startOfCurr){
      prev = intervals[i];
    } else{
      countRemove =+ 1;
    }
  }
  return countRemove;
}