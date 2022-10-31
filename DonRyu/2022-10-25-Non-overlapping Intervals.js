const eraseOverlapIntervals = function (intervals = []) {
  if (!intervals.length) {
    return 0
  }
  intervals.sort((a, b) => a[1] - b[1])
  let prevEnd = intervals[0][1]
  let count = 1
  for (const [a, b] of intervals) {
    if (a >= prevEnd) {
      count += 1
      prevEnd = b
    }
  }
  return intervals.length - count
}
