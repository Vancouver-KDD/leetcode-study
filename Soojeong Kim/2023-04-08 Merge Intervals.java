import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        List<int []> result = new ArrayList<>();

        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));

        int [] list = new int[2];
        list[0] = intervals[0][0];
        int preMax = intervals[0][1];

        for(int i = 1; i<intervals.length;i++) {
            if(intervals[i][0]>preMax) {
                //non-overlapping case
                list[1] = preMax;
                result.add(list);
                list = new int[2];
                list[0] = intervals[i][0];
                preMax = intervals[i][1];
            }else {
                //overlapping case
                preMax = Math.max(preMax, intervals[i][1]);
            }
        }
        list[1] = preMax;
        result.add(list);

        return result.toArray(new int[result.size()][2]);
    }
}

//TC: O(nlogn)