
//2023-10-04
//idea: 
//  1) First, sort the input points by the end coordinate. 
//  2) Initiate number of arrows => 1,  previous end => points[0][1]
//  3) Iterate over all input points like below:
//      if the current points starts after previous end
//      => arraows => arrows + 1  , previous end  => current end
//<example>
//  input: [[10,16],[2,8],[1,6],[7,12]] -> 2
//  input: [[-2147483648,2147483647]] -> 1   
//  input: [[-2147483646,-2147483645],[2147483646,2147483647]] -> 2
//Time Complexity: O(NlogN) <-- sort time 
//Space Complexity: O(N)<-- the space for sorting
class Solution {
    public int findMinArrowShots(int[][] points) {
        if(points == null || points.length <= 0){
            return 0;
        }
        
        // We can't simply use the a[1] - b[1] trick, as this will cause an 
        // integer overflow for very large or small values.
        //Arrays.sort(intervals, (a,b)->(a[1]-b[1]) );
        Arrays.sort(points, (a,b)->{
            if( a[1] < b[1]){
                return -1;
            }else if( a[1] ==b[1]){
                return 0;
            }else{
                return 1;
            }
        }); 
        
        int arrows = 1;
        int prevEnd = points[0][1];
        //-2^31 <= xstart < xend <= 2^31 - 1 라는 boundary 때문에 prevEnd = Integer.MIN_VALUE 로 놓고 
        // for 문을 0 부터 시작하면 input: [[-2147483648,2147483647]] 인 경우 문제 생김. 
        
        //points = [[10,16],[2,8],[1,6],[7,12]] ->[[1,6],[2,8],[7,12],[10,16]]
        //prevEnd: 6,12, 
        //overlap: 0, 1, 2
        for(int i = 1; i < points.length ; i++){
            int nextStart = points[i][0];
            if(prevEnd < nextStart  ){
                prevEnd = points[i][1];
                arrows++;
            }
        }
        
        return arrows;
    }
}