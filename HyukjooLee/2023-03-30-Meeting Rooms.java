// Given an array of meeting time intervals where intervals[i] = [starti, endi],
// determine if a person could attend all meetings.

// Example 1:

// Input: intervals = [[0,30],[5,10],[15,20]]
// Output: false
// Example 2:

// Input: intervals = [[7,10],[2,4]]
// Output: true

// determine whether a person could attend all meetings based on an array of meeting time intervals

// sort the intervals based on their starting times
// iterate through the sorted intervals
// if the starting time of the current interval is less than or equal to the ending time of the previous interval, 
// return false because the person cannot attend overlapping meetings
// otherwise, continue iterating through the intervals
// if we reach the end of the loop without finding any overlapping intervals, return true
// time complexity: O(NlogN) = sorting step
// space complexity: O(1) for constant space
public int eraseOverlapIntervals(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    int previousEndTime = -1;
    for (int[] interval : intervals) {
        int startTime = interval[0];
        int endTime = interval[1];
        if (startTime < previousEndTime) {
            return false;
        }
        previousEndTime = endTime;
    }
    return true;
}