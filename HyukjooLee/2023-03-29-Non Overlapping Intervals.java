// Given an array of intervals intervals where intervals[i] = [starti, endi], 
// return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

// Example 1:

// Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
// Output: 1
// Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

// determine the minimum number of intervals that need to be removed to make the rest of the intervals non-overlapping


// initialize a counter variable to 0 and a variable to store the ending time of the last interval 
// in the non-overlapping set to the minimum possible value.
// iterate through the sorted intervals
// if the starting time of the current interval is greater than or equal to the ending time of the last interval in the non-overlapping set, 
// add the current interval to the non-overlapping set and update the last interval ending time.
// otherwise, increment the counter variable and skip adding the current interval to the non-overlapping set.
// the counter variable represents the minimum number of intervals that need to be removed to make the rest non-overlapping.
// time complexity: O(NlogN) = sorting step
// space complexity: O(1) for constant space
public int eraseOverlapIntervals(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[1] - b[1]); // sort the intervals based on their ending times
    // store the ending time of the last interval 
    int count = 0; 
    int lastEnd = Integer.MIN_VALUE;

    for (int[] interval : intervals) {
        int start = interval[0];
        int end = interval[1];
        if (start >= lastEnd) {
            lastEnd = end;
        } else {
            count++;
        }
    }
    return count;
}
