/*
 * https://leetcode.com/problems/non-overlapping-intervals/
 * 
 * ## Description 
 * Given an array of intervals intervals where intervals[i] = [start(i), end(i)], return the minimum number of intervals you need to remove to make the rest of * the intervals non-overlapping.
 */

//[1,2] [3,9] [4,6] [8,10]
//after sorting: [1,2] [4,6] [3,9] [8,10]
//i = 1, prev = 0 : 4 >= 2 (true) => move both pointers and count (keep both)
//i = 2, prev = 1 : 3 >= 6 (false) => move i pointer only (removing interval[i](right array))
//i = 3, prev = 1 : 8 >= 6 (true) => count and done! 

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int n = intervals.length; 

        //Sort the array by the end element 
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[1], b[1]));
        
        int count = 1; // store the non-overlapping array elements. 
                    // count the first array to the result non-overlapping array
        int prev = 0; //will point the previous array 

        //iterate all the array 
        for(int i = 1; i < n; i++ ) {
            if(intervals[i][0] >= intervals[prev][1]) {
                prev = i; //move the pointer as keeping both compared arrays 
                count++; //count non-overlapping array 
            }
        }
        return n - count; // return the number of array need to be removed. 
    }
}