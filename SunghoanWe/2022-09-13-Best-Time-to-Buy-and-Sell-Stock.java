public class BestTimetoBuyandSellStock {
	public static void main(String args[]) {
		int[] prices = {7,1,5,3,6,9};
		System.out.println(new BestTimetoBuyandSellStock().maxProfit(prices));
		
	}

// Time Limit Exceeded	
//    public int maxProfit(int[] prices) {
//    	int maxProfit = 0;
//    	for (int i=0; i < prices.length-1; i++) {
//    		for (int j=i+1; j < prices.length; j++) {
//    			int temp = prices[j] - prices[i];
//    			if (maxProfit < temp) {
//    				maxProfit = temp;
//    			}
//    		}
//    	}
//    	
//    	return maxProfit;
//    }
    
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;
        for (int i = 0; i < prices.length; i++) {

            if (prices[i] < minPrice) {
                minPrice = prices[i];
        	} else if (prices[i] - minPrice > maxProfit) {        	
                maxProfit = prices[i] - minPrice;
            } 
        }
        return maxProfit;
    }
}
