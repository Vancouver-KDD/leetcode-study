public class Solution {
    public int MaxProfit(int[] prices) {
        
        int max = 0;
        int maxProfit = 0;

        for(int i = prices.Length-1; i>=0;i--){
            max= Math.Max(max,prices[i]);
            maxProfit= Math.Max(maxProfit,max - prices[i] );
        }

        return maxProfit;
    }
}

//Time complexity: O(n);
//Space complexity: O(1);
