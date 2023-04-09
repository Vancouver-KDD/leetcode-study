//interval scheduling
//The interval scheduling maximization problem (ISMP) is 
//to find a largest compatible set, i.e., a set of non-overlapping intervals of maximum size.
//참고 : https://snupi.tistory.com/34
//https://en.wikipedia.org/wiki/Interval_scheduling#Interval_Scheduling_Maximization

import java.util.*;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        //end로 비교하기
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[1], i2[1]));
        int end = intervals[0][1];
        int count = 1;

        for(int i = 1; i<intervals.length;i++){
            if(intervals[i][0]>=end) {
                end = intervals[i][1];
                count++;
            }
        }
        return intervals.length-count;
    }
}
//Tc : O(NlogN)
