Class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int n = intervals.length;
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1])); // sort by max value of each interval

        int prev = 0;
        int count = 1;

        for (int i = 1; i < n; i++) {
            // count the valid intervals
            if (intervals[i][0] >= intervals[prev][1]) { // compare min value of each interval with max value of previous interval
                prev = i; // update prev to current interval
                count++;
            }
        }
        return n - count;

       
        
    }
}