
//2023-09-28
//Idea:  HashMap + Sliding Window => 여기서 HashMap<Value, Value 나타난횟수>
//Time Complexity : O(N)
//Space Complexity : O(1) , HashSet 사이즈가 2 로 고정.
class Solution {
    public int totalFruit(int[] fruits) {
        
        if(fruits == null || fruits.length <= 0){
            return 0;
        }
        
        Map<Integer, Integer> basket = new HashMap<>(); //<key, value> =< type, count>
        
        int start = 0;
        int longest = 0;
        for(int end = 0; end < fruits.length; end++){
            
            basket.put(fruits[end], basket.getOrDefault(fruits[end],0) + 1);
            
            while(basket.size() > 2){
                int key = fruits[start];
                basket.put(key, basket.get(key) - 1);
                if(basket.get(key) == 0){
                    basket.remove(key);
                }
                start++;
            }
            longest = Math.max(longest, end - start + 1);
        }
        return longest;
    }
}