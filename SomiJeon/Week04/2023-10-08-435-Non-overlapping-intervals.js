// Given an array of intervals intervals where intervals[i] = [starti, endi],
//todo: return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

//* Example 1:

// Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
// Output: 1
// Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

//* Example 2:

// Input: intervals = [[1,2],[1,2],[1,2]]
// Output: 2
// Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

//* Example 3:

// Input: intervals = [[1,2],[2,3]]
// Output: 0
// Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function (intervals) {
  if (intervals.length === 0) return 0;

  // Sort intervals by end times
  intervals.sort((a, b) => a[1] - b[1]);

  let count = 1; // Initialize with one interval since the first interval is always included
  let end = intervals[0][1];

  for (let i = 1; i < intervals.length; i++) {
    const currentInterval = intervals[i];
    const start = currentInterval[0];

    if (start >= end) {
      // The current interval doesn't overlap with the last non-overlapping interval
      count++;
      end = currentInterval[1];
    }
    // If the current interval overlaps with the last non-overlapping interval, skip it
  }

  // Calculate the number of intervals to remove
  const removeCount = intervals.length - count;
  return removeCount;
};
