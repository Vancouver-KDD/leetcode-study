class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        1. list of trees
            1, 2, 3, 4, 5
            left to right
        2. You have two baskets, you can put only one type of fruit into a basket.
        3. Baskets has no limit on the amount of fruit they can hold
        4. when you get to each tree, you must pick one fruit. 
            1. you can start from any tree you want.
        5. if you can not put fruit into your baskets due to tpye problem, looping must stop.
        6. Find maximum number of fruits you can pick and return it. 
        
        strategy
        -find longest window
        -When you encounter a new type of tree, move the left pointer to the position where the first 
        occurrence of the second most recent type (type[right-1]).
        -keep moving to the left until the end of the type
        """
        if len(fruits) == 1:
            return 1
        
        baskets = set()
        left = 0
        res = 0
        for right in range(len(fruits)):
            if len(baskets) < 2:
                baskets.add(fruits[right])
                continue
            if fruits[right] not in baskets:
                baskets.clear()
                baskets.add(fruits[right])
                baskets.add(fruits[right - 1])
                res = max(res, right - left)
                left = right - 1
                while fruits[left] in baskets:
                    left -= 1
                left += 1
        res = max(res, len(fruits) - left)
        return res




        class Solution {
    public int totalFruit(int[] fruits) {
      	int l = 0;
      	int maxSizeOfBasket = 2;
      	int maxNumberOfFruits = 0;
      	int curNumberOfFruits = 0;
        // data structure to store two different fruits
      	Map<Integer, Integer> basket = new HashMap<>();
		
      	for (int r = 0; r < fruits.length; ++r) {
      		// keep adding the new type of fruit until encountering another type of fruit
          	basket.put(fruits[r], basket.getOrDefault(fruits[r], 0) + 1);
          	curNumberOfFruits++;

            while (basket.size() > maxSizeOfBasket) { // if encounter the third type of fruit, remove the first type of fruit [1(l), 2, 3, 2, 2]
                  Integer fruitToBeRemoved = fruits[l];
                  basket.put(fruitToBeRemoved, basket.get(fruitToBeRemoved) - 1); // decrease the first type of the fruit
                  curNumberOfFruits--;
                  l++;
                  if (basket.get(fruitToBeRemoved) == 0) basket.remove(fruitToBeRemoved); // if the basket has no more fruit, remove it
            }

            maxNumberOfFruits = Math.max(maxNumberOfFruits, curNumberOfFruits);
         }
    		
      	return maxNumberOfFruits;
    }
}