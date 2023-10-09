import java.util.ArrayList;
import java.util.List;

/**
Time Complexity: O(M + N) , M = firstList.length && N = secondList.length
Space Complexity: O(M + N). Max size of result
 */
class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> result = new ArrayList<>();

        //pointers to firstList and secondList respectibly
        int i = 0; 
        int j = 0;

        while(i < firstList.length && j < secondList.length) {
          int firstEnd = firstList[i][1];
          int secondEnd = secondList[j][1];
          if(firstEnd > secondEnd) {
            if(firstList[i][0] <= secondEnd) {
              //add to result if intersection exists
              //result.put([Math.max(firstList[i][0],secondList[i][0]),secondEnd]);
              result.add(new int[]{Math.max(firstList[i][0],secondList[j][0]), secondEnd});
            }
            
            j++;
          } else {
            //add to result if intersection exists
              if(secondList[j][0] <= firstEnd) { 
                //add to result if intersection exists
                //result.put([Math.max(firstList[i][0],secondList[i][0]),secondEnd]);
                result.add(new int[]{Math.max(firstList[i][0],secondList[j][0]), firstEnd});

              }
            i++;
          }
        }

        //change ArrayList to int[][]
        return result.toArray(new int[result.size()][]);
    }
}