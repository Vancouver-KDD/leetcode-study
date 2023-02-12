
//limitation : prices is null. 
//Input: prices = [7,1,5,3,6,4]  --> Output; 5

//2023-01-25
//[idea] : save lowest number , get differece if current number is bigger than lowest number. 
//Similar Question: 2012. Sum of Beauty in the Array
//Time Complexity: O(N)
//Space Complexity: O(1)

class Solution{
    public int maxProfit(int[] prices){
        if(prices == null || prices.length == 0){
            return 0;
        }

        //prices = [7,   1,   5,   3,   6,   4]
        //lowest:   7 -> 1 -> 1 -> 1 -> 1 -> 1
        //maxPrice: 0 -> 0 -> 4 -> 4 -> 5 -> 5
        int maxPrice = 0;
        int lowest = prices[0];
        for(int i = 1; i < prices.length; i++){
            if(lowest > prices[i]){
                lowest = prices[i];
            }else{
                int currentPrice = prices[i] - lowest;
                maxPrice = Math.max(maxPrice, currentPrice);
            }
        }

        return maxPrice;
    }
}
//Time Complexity: O(N), Space Complexity : O(1)
//2022.12.02
//Time Complexity: O(N)
//Space Complexity: O(1)
/*
class Solution{
    public int maxProfit(int[] prices){
        if(prices == null || prices.length == 0){
            return 0;
        }

        int profit = 0;
        int minPrice = prices[0];
        for(int i = 1; i < prices.length; i++){
            minPrice = Math.min(minPrice, prices[i]);
            if(minPrice > prices[i]){
                minPrice = prices[i];
            }else{
                int tempProfit = prices[i] - minPrice;
                profit = Math.max(profit, tempProfit);
            }

        }

        return profit;
    }
}
*/
//2022.09.11
/*
class Solution {
    public int maxProfit(int[] prices) {
        
        if(prices == null || prices.length == 0){
            return 0;
        }
        
        int maximumProfit = 0; 
        int lowestTransaction = prices[0];
        for(int i = 1; i < prices.length; i++){
            
            if(prices[i] < lowestTransaction){ 
                lowestTransaction = prices[i];
            }else{
                maximumProfit = Math.max(maximumProfit, prices[i] - lowestTransaction); 
            }    
        }
        
        return maximumProfit;
    }
}
*/
//2022.07.07
/*
class Solution {
    public int maxProfit(int[] prices) {
        
        if(prices == null || prices.length == 0){
            return 0;
        }
        
        int min = prices[0];
        int maxProfit = 0;
        int profit = 0;
        for(int i = 0; i < prices.length; i++){
            profit = prices[i] - min;
            if(profit > maxProfit){
                maxProfit = profit;
            }
            if(prices[i] < min){
                min = prices[i];
            }
            
        }
        
        return maxProfit;
    }
}
*/



//input : [7,1,5,3,6,4] -> output: 5
// Time complexity : O(N), Space complexity: O(1)
/*
class Solution {
    public int maxProfit(int[] prices) {
     
        if(prices == null || prices.length == 0){
            return 0;
        }

        int buy = Integer.MAX_VALUE;
        int maxProfit = 0;
        for(int i = 0; i < prices.length; i++){
            
            buy = Math.min(buy, prices[i]);
            
            int profit = prices[i] - buy;
            maxProfit = Math.max(maxProfit, profit);

        }

        return maxProfit; 
    }
}
*/
/*
class Solution {
    public int maxProfit(int[] prices) {
     
        int largestDiff = 0;
        int minBuy = Integer.MAX_VALUE;
        
        for(int i = 0; i< prices.length; i++){
                      
                                    
            if(minBuy > prices[i]){
                minBuy = prices[i];                
            }
            
            largestDiff = Math.max(largestDiff, prices[i] - minBuy);

        }
        
        return largestDiff;

    }
}
*/

//Below solutio is failed because of time limitation--------
/*
class Solution {
    public int maxProfit(int[] prices) {
     
        int max = 0;
        
        for(int i = 0; i< prices.length; i++)
            for(int j = i+1; j < prices.length; j++){
                int profit = prices[j] - prices[i];
                if(max < profit){
                    max = profit;
                }
            }
        
        return max;

    }
}
*/