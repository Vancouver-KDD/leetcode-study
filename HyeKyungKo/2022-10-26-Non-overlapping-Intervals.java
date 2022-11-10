//Similar questions
//  452. Minimum Number of Arrows to Burst Balloons  (premium)
//  
// 어떤식으로 overlapping 되지? 
//  [[1,2],[1,3]] <-- 이런식으로 완전히 포함관계의 overlapping 인지 
//  [[1,5],[3,6]] <-- 이런식으로 걸치는 overlapping 도 있는건지 -> 이경우도 존재. 
//                  합치는건 아니고 overlapping 되는게 있으면 remove 만 함. 그럼 앞에것과 뒤엣것중 아무거나???
//  input: [[1,3],[4,7],[1,7]] -> output: 1
//  input: [[1,5],[3,8],[5,8]] -> output: 1
//  input: [[0,2],[1,3],[2,4],[3,5],[4,6]] -> output: 2

//Time Complexity: O(nlon) <-- sort time 
//Space Complexity: O(1)
class Solution{
    public int eraseOverlapIntervals(int[][] intervals){
        if(intervals == null || intervals.length == 0){
            return 0;
        }
        
        //sort by ascendgin order of 'end'
        Arrays.sort(intervals, (a,b)->(a[1] - b[1]));
        
        int size = intervals.length;
        int count = 1;
        int end = intervals[0][1];
        
        //find non-overlapping 
        for(int i = 1; i < size; i++){
            if(intervals[i][0] >= end){
                end = intervals[i][1]; //update the value for end
                count++;
            }
        }
        
        // size -count = the number of overlapping that need to remove 
        return size - count;
    }
}

/*
//idea: 
//1) sort by the ascending order of 'start'
//2) set 'each nonOverlap' as 1
//3) compare previous 'end' continuously to find 'end' <= 'start' -> then count++
//4) total number - count = minimum number of intervals to remove

//Time Complexity: O(n^2)
//Space Complexity: O(n)
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        
        if(intervals == null || intervals.length == 0){
            return 0;
        }
        
        //sort by ascending order of 'start'
        Arrays.sort(intervals, (a,b)->(a[0] - b[0]));
        
        int nonOverlap = 1;
        int[] maxNonOverlap = new int[intervals.length];
        maxNonOverlap[0] = 1;
        
        for(int i = 1; i < intervals.length; i++){
            maxNonOverlap[i] = 1;
               for(int j = i-1; j >=0; j--){
                   if(intervals[i][0] >= intervals[j][1]){ //non-overlapping
                       
                        maxNonOverlap[i] = maxNonOverlap[j] +1;
                        break;                 
                   }
               }
        }
        
        return intervals.length - maxNonOverlap[intervals.length-1];
        
    }
    
}
*/