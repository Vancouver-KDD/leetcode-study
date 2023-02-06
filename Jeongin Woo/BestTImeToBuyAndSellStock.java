
public class BestTImeToBuyAndSellStock {
	  public int maxProfit(int[] prices) {
	        int max = 0;
	        int buy = prices[0];
	        int sell = 0 ;
	        for(int i =0; i < prices.length;i++)
	        {
	            buy = Math.min(buy,prices[i]);
	            sell = Math.max(sell,prices[i]-buy);
	        }

	        return sell;
	    }


}
