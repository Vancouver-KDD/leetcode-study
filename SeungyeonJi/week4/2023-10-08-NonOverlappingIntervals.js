var eraseOverlapIntervals = function (intervals) {
  if (intervals.length < 0) return 0;

  intervals.sort((a, b) => a[1] - b[1]);

  let end = 0;
  let counter = 0;

  for (let i = 1; i < intervals.length; i++) {
    let pre = intervals[end];
    let current = intervals[i];

    if (pre[1] > current[0]) {
      counter++;
    } else {
      pre[1] = current[1];
    }
  }
  return counter;
};
