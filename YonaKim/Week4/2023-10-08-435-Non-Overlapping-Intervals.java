import java.util.Arrays;
import java.util.Comparator;

/**
Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 */

/**
Time Complextiy: O(nlog(n)) - sort(Object[]) accepts reference types. Arrays. sort(Object[]) is based on the TimSort algorithm, giving us a time complexity of O(n log(n)).

Space Complexity: O(logn) - In Java, Arrays.sort() is implemented using a variant of the Quick Sort algorithm, which has a space complexity of O(log⁡n)O(\log n)O(logn).
 */
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int minOverlap = 0;
        int helper = Integer.MIN_VALUE;

        //sort intervals in ascending end order (intervals = [[start,end],[start2,end2],..])
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[1]));

        for(int i = 0; i < intervals.length; i++) {
            //intervals = [[x,y],[x2,y2],..]
            int x = intervals[i][0];
            int y = intervals[i][1];

            if(x >= helper) {
                helper = y;
            } else {
                minOverlap++;
            }
        }

        return minOverlap;
    }
}