//Input: prices = [7,1,5,3,6,4]  --> Output; 5
//Time Complexity: O(N), Space Complexity : O(1)

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