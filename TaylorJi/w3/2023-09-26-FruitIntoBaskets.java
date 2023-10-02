class Solution {
    public int totalFruit(int[] fruits) {
    
        HashMap<Integer, Integer> map = new HashMap();

        int i = 0;
        int ans = 0;

        for (int j = 0; j < fruits.length; j++) {
            map.put(fruits[j], map.getOrDefault(fruits[j], 0) + 1); // if the same type of the fruit, simply increment 
            
            if (map.size() > 2) {
                map.put(fruits[i], map.get(fruits[i]) - 1); // decrement the first type of fruit
                if (map.get(fruits[i]) == 0) {
                    map.remove(fruits[i]);
                }
                i++;
            }
            ans = Math.max(ans, j - i + 1);
        }
        return ans;
    }
}