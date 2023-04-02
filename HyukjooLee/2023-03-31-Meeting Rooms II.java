// Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], 
// return the minimum number of conference rooms required.

 

// Example 1:

// Input: intervals = [[0,30],[5,10],[15,20]]
// Output: 2

public int minMeetingRooms(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    PriorityQueue<Integer> endTimes = new PriorityQueue<>();
    for (int[] interval : intervals) {
        int startTime = interval[0];
        int endTime = interval[1];
        if (!endTimes.isEmpty() && startTime >= endTimes.peek()) {
            endTimes.poll();
        }
        endTimes.offer(endTime);
    }
    return endTimes.size();
}
