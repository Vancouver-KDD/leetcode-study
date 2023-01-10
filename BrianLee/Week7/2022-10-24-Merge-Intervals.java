class Solution {
    public int[][] merge(int[][] intervals) {
        Queue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        for(int[] interval : intervals) pq.add(interval);

        List<int[]> results = new ArrayList<>();
        int[] interval = pq.poll();
        int start = interval[0];
        int end = interval[1];
        while(!pq.isEmpty()) {
            interval = pq.poll();
            if(interval[0] <= end) {
                end = Math.max(end, interval[1]);
            } else {
                results.add(new int[]{start, end});
                start = interval[0];
                end = interval[1];
            }
        }
        results.add(new int[]{start, end});

        int[][] mergeResult = new int[results.size()][2];
        for(int i = 0; i < results.size(); i++) {
            mergeResult[i] = results.get(i);
        }
        return mergeResult;
    }
}