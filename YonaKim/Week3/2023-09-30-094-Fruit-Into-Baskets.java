//Sliding Windows algorithm

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int totalFruit(int[] fruits) {
        int maxResult = 0;
        Map<Integer,Integer> baskets = new HashMap<>();
        int windowStart = 0;

        for(int windowEnd = 0; windowEnd < fruits.length; windowEnd++) {
            baskets.put(fruits[windowEnd], baskets.getOrDefault(fruits[windowEnd],0)+1);
            while(baskets.size() > 2) {
                baskets.put(fruits[windowStart], baskets.getOrDefault(fruits[windowStart],0)-1);
                if(baskets.get(fruits[windowStart]) == 0) {
                    baskets.remove(fruits[windowStart]);  
                }
                windowStart++;
            }

            maxResult = Math.max(maxResult, (windowEnd - windowStart + 1));
        }

        return maxResult; 
    }
}