// Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
// and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

// Example 1:

// Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


// 모든 겹치는 간격을 merge
// 겹치지 않는 간격의 새 배열을 반환

// 1, 3]: The interval from time 1 to time 3.
// [2, 6]: The interval from time 2 to time 6 => overlapping with the previous interval [1,3].
// [8, 10]: The interval from time 8 to time 1 => not overlapping
// [15, 18]: The interval from time 15 to time 18 => not overlapping

// Sort the intervals based on their starting points.
// Create a result list to hold the non-overlapping intervals.
// Iterate through the sorted intervals:
// If the current interval overlaps with the last interval in the result list, 
// merge them by updating the end point of the last interval.
// Otherwise, add the current interval to the result list.
// Return the result list.

// time complexity: O(NlogN) = sorting step
// space complexity: O(N) for the result list
public int[][] mergeIntervals(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    List<int[]> mergedIntervals = new ArrayList<>();
    int[] previousInterval = null;
    for (int[] interval : intervals) {
        if (previousInterval == null || interval[0] > previousInterval[1]) {
            mergedIntervals.add(interval);
            previousInterval = interval;
        } else {
            previousInterval[1] = Math.max(previousInterval[1], interval[1]);
        }
    }
    return mergedIntervals.toArray(new int[mergedIntervals.size()][]);
}