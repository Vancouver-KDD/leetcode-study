import java.util.*;

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int []> result = new ArrayList<>();
        int [] list = newInterval;
        
        for(int i = 0; i<intervals.length;i++) {
            //경우의 수
            if(newInterval[1]<intervals[i][0]) {
                //interval 안에 newinterval 들어가는 경우
                result.add(list); 
                list = intervals[i];
            }else if(intervals[i][1]>=list[0]){
                //interval에 걸치게 될 때
                list = new int[] {
                    Math.min(intervals[i][0], list[0] ),
                    Math.max(intervals[i][1], list[1])
                };
            }else {
                //이제부터는 newinterval을 포함하고 있는 list
                result.add(intervals[i]);
            }
        }
        result.add(list);
        return result.toArray(new int[result.size()][2]);
    }
}