class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,(arr1,arr2) -> arr1[1] - arr2[1]);
        int answer = 0;
        int prev = intervals[0][1];
        for(int i=1; i<intervals.length; i++){
            if(prev > intervals[i][0]){
                answer++;
            }else{
                prev=intervals[i][1];
            }
        }
        
    return answer;
    }
}