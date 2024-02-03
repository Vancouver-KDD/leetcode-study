// https://leetcode.com/problems/fruit-into-baskets/description/

class Solution {
    public int totalFruit(int[] fruits) {
        Map<Integer,Integer> baskets = new HashMap<>();

        int start = 0;
        int max = 0;
        for(int end = 0; end < fruits.length; end++) {
            baskets.put(fruits[end], baskets.getOrDefault(fruits[end], 0) + 1);

            while(baskets.size() > 2) {
                baskets.put(fruits[start], baskets.get(fruits[start])-1);
                if(baskets.get(fruits[start]) == 0) baskets.remove(fruits[start]);
                start++;
            }

            // loop 2 values
            // int current = 0;
            // for(Integer count: baskets.values()) current += count;
            // max = Math.max(max, current);

            max = Math.max(max, end - start + 1);
        }

        return max;
    }
}