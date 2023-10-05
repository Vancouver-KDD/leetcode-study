
//2023-10-04
//merge Intervals
//Time Complexity: O(N+M)
//Space Complexity: O(N+M) <-- it is for return array
class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        
        
        if(firstList == null || firstList.length <= 0 || secondList == null || secondList.length <= 0){
            return new int[0][0];
        }
        
        List<int[]> intersectList = new ArrayList<>();
        
        int fcount = 0;
        int scount = 0;
        while(fcount < firstList.length && scount < secondList.length){
            int start = Math.max(firstList[fcount][0], secondList[scount][0]);
            int end = Math.min(firstList[fcount][1], secondList[scount][1]);
            if(start <= end){
                intersectList.add(new int[]{start, end});
            }  
            fcount = (end == firstList[fcount][1]) ? fcount+1 : fcount;
            scount = (end == secondList[scount][1]) ? scount+1 : scount;
        }
        
        int[][] intersectArray = intersectList.toArray(new int[intersectList.size()][]);
        return intersectArray;
    }
}                                                                                                       