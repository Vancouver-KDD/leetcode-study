class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Queue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        for(int[] interval : intervals) pq.add(interval);

        int count = 0;
        int[] interval = pq.poll();
        int start = interval[0];
        int end = interval[1];

        while(!pq.isEmpty()) {
            interval = pq.poll();
            if(interval[0] < end) {
                end = Math.min(end, interval[1]);
                count++;
            } else {
                start = interval[0];
                end = interval[1];
            }
        }
        return count;
    }
}