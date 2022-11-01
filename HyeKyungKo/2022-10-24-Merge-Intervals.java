//similar Question
//  252. Meeting Rooms (premium)
//  763. Partition Labels
//  57. Insert Interval (premium)

//2022-10-24
//limitation: [[s1,e1],[s2,e2],[s3,e3],...] <--- s1<=s2<=s3<=... 이순서가 보장되는건가? => 보장이 안되는구만...
//Input: intervals = [[1,3],[2,6],[8,10],[15,18]] -> output: [[1,6],[8,10],[15,18]]
//Input: intervals = [[1,4],[4,5]] -> output: [[1,5]]
//Input: intervals = [[1,4],[0,4]] -> output: [[0,4]]
//Input: intervals = [[1,4],[2,3]] -> output: [[1,4]]

//Idea: 
//  0) 순서가 보장이 안되면 ... Sort 부터 해야함. 
//  1) List<List<Integer>>() 생성  
//  2) i 번째 e 와 i+1 의 s 를 비교, 겹치면 합치기 
//  3) 더이상 겹치지 않으면 1)번 list 에 넣기

// Time Complexity : O(nlogn) <--- sort 시간 
// Space Complexity : O(logn) or O(n) <--- sort 에서 쓴 space

//leetcode 풀이보고 수정
class Solution{
    public int[][] merge(int[][] intervals){
        
        if(intervals.length == 0){
            return new int[0][]; //return empty array
        }
        
        //sort by acending order of first value
        Arrays.sort(intervals, (a,b)->(a[0] - b[0])); // a:int[2], b:int[2]
        
        List<int[]> mergedList = new ArrayList<int[]>();
        
        mergedList.add(intervals[0]);
        
        for(int i = 1; i < intervals.length; i++){
            int[] last = mergedList.get(mergedList.size()-1); 
            if(intervals[i][0] <= last[1]){ //overlapping
                last[1] = Math.max(last[1], intervals[i][1]);
            }else{ // no overapping
                mergedList.add(intervals[i]);
            }                                                       
        }
        
        //make 2d array from list
        int[][] mergedArray = mergedList.toArray(new int[mergedList.size()][]);
        
        return mergedArray;
    }    
}
/*
class Solution{
    public int[][] merge(int[][] intervals){
        
        List<int[]> merged = new ArrayList<int[]>();
        
        if(intervals.length == 0){
            return new int[0][]; //return empty array 
        }
        
        //sorting by ascending order of 'start'
        Arrays.sort(intervals, (a,b)->(a[0] - b[0])); //a = int[2] , b = int[2]
        
        int start = intervals[0][0];
        int end = intervals[0][1];
        for(int i = 1; i < intervals.length; i++){
            if(intervals[i][0] <= end){ //overlapping
                end = Math.max(end, intervals[i][1]); //choose max end.
            }else{
                merged.add(new int[]{start,end});
                start = intervals[i][0];
                end = intervals[i][1];
            }
        }
        
        //add last intervals
        merged.add(new int[]{start,end});
        
        //int[][] resultArray = new int[merged.size()][2];
        //for(int i = 0; i < merged.size(); i++){
        //    int[] interval = merged.get(i);
        //    resultArray[i][0] = interval[0];
        //    resultArray[i][1] = interval[1];
        //}
        
        int[][] resultArray = merged.toArray(new int[merged.size()][]);

        
        return resultArray;
    }
}
*/

//leetcode solution 
/*
class Solution {
    public int[][] merge(int[][] intervals) {
        if(intervals.length <= 1){
            return intervals;
        }
        
        Arrays.sort(intervals, (a,b)->Integer.compare(a[0],b[0]));
        
        LinkedList<int[]> mergedList = new LinkedList<>();
        
        for(int[] value : intervals){
            if(mergedList.isEmpty()){
                mergedList.add(value);
            }else{
                int[] lastList = mergedList.getLast();
                if(lastList[1] < value[0]){
                    mergedList.add(value);
                }else{
                    lastList[1] = Math.max(lastList[1], value[1]);
                }
            }
            
        }
        
        int[][] mergedArray = mergedList.toArray(new int[mergedList.size()][]);
        
        return mergedArray;
    }
}
*/
