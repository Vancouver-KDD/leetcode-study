class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {

        Arrays.sort(intervals, (i1, i2) -> i1[0] - i2[0]);

        int count = 0;

        int prevEnd = intervals[0][1];
        for (int i = 1; i < intervals.length; i++) {
            int[] curr = intervals[i];
            if (curr[0] < prevEnd) {
                prevEnd = Math.min(prevEnd, curr[1]);
                count += 1;
            }
            else prevEnd = curr[1];
        }
        return count;
    }
}