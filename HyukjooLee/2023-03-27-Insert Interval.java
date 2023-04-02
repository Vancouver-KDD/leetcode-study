// You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
// represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
// You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

// Insert newInterval into intervals such that intervals is still sorted in ascending order
// by starti and intervals still does not have any overlapping intervals 
// (merge overlapping intervals if necessary).

// Return intervals after the insertion.


// Example 1:

// Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
// Output: [[1,5],[6,9]]

// sorted & non-overlapping interval list 에 새 간격을 삽입
// 필요한 경우에는 overlapping 되는 간격을 병합해야 하는 문제
// output should be sorted & non-overlapping interval as well

// iterating over the interval list and comparing the start and end times of each interval with the new interval
// if the new interval overlaps with the current interval, we merge the two intervals and move on to the next interval
// if the new interval does not overlap with the current interval, we add the current interval to the output list and continue iterating
// when we find the correct position to insert the new interval,
// insert it into the output and continue iterating to merge any further overlapping intervals
// The time complexity is O(N); the length of the input list
// The space complexity is O(N); since we need to store the output interval list
public int[][] insertInterval(int[][] intervals, int[] newInterval) {
    List<int[]> result = new ArrayList<>();
    int index = 0;
    int length = intervals.length;
    
    // add all intervals that come before the new interval
    while (index < length && intervals[index][1] < newInterval[0]) {
        result.add(intervals[index]);
        index++;
    }
    
    // merge all overlapping intervals with the new interval
    while (index < length && intervals[index][0] <= newInterval[1]) {
        newInterval[0] = Math.min(newInterval[0], intervals[index][0]);
        newInterval[1] = Math.max(newInterval[1], intervals[index][1]);
        index++;
    }
    result.add(newInterval);
    
    // add all intervals that come after the new interval
    while (index < length) {
        result.add(intervals[index]);
        index++;
    }
    
    // convert the list to an array and return it
    return result.toArray(new int[result.size()][]);
}
