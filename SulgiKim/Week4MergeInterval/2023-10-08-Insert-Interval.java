/*
 * https://leetcode.com/problems/insert-interval/
 * 
 * ## Description 
 * You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and 
 * intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another 
 * interval.
 * 
 * Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping
 * intervals (merge overlapping intervals if necessary).
 * 
 * Return intervals after the insertion.
 */


class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        //Initialize the output array - use ArrayList cuz we don't know the size yet. 
        List<int[]> output = new ArrayList<>();
				
        int newStart = newInterval[0], newEnd = newInterval[1];
        boolean insert = false; 
				
				//Iterate through all the interval in intervals array. 
        for (int[] interval : intervals) {
            int currStart = interval[0], currEnd = interval[1]; 
            
						//when the current interval is non-overlapping with newInterval and smaller overall, add the interval to output array. 
            if(currEnd < newStart) { 
                output.add(interval); 
						//when the current interval is non-overlapping with newInterval and bigger overall, add the interval to output array. 
            } else if (currStart > newEnd) {   
								//check if the updated value of newInterval has been added into the output array. 
                if(!insert) {
                    output.add(new int[]{newStart, newEnd});
                    insert = true; //update the insert value to true so we don't add it again. 
                }
                output.add(interval); 
						//when current interval and newInterval are overlapping, update the newInterval value, taking minimum for start and maximum for end 
            } else {
                newStart = Math.min(currStart, newStart);
                newEnd = Math.max(currEnd, newEnd);
            }
        }
				
				//just in case if there was any condition met while looping (ex. when interval is empty), add the newInterval. 
        if(!insert) {
            output.add(new int[]{newStart, newEnd});
        }

        return output.toArray(new int[output.size()][]);
    }
}