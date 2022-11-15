public class Solution {
    public int MaxProfit(int[] prices) {
        int buyPrice = prices[0];
        int maxProfit = 0;
        
        
        foreach(int p in prices){
            
            if(p - buyPrice > maxProfit){
                maxProfit = p - buyPrice;
            }
            
            if(p < buyPrice){
                buyPrice = p;
            }
        }
        
        return maxProfit;
    }
}