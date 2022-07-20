function merge(intervals){
  // sort them by zero index
  intervals.sort((a,b) => a[0] - b[0]);
  // create result array and put in the first intervals as an initial value
  const result = [intervals[0]];

  // iterate over this array and update the result
  for(let interval of intervals){
    let endOfResult = result[result.length - 1][1];
    let secondStartOfInterval = interval[0];
    let secondEndOfInterval = interval[1];

    if(endOfResult >= secondStartOfInterval){       // need to merge
      result[result.length - 1][1] = Math.max(endOfResult, secondEndOfInterval);
    } else{
      result.push(interval);
    }
  }
  return result;
}