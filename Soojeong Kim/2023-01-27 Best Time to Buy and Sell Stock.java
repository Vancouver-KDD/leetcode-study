class Solution {
    public int maxProfit(int[] prices) {
        int min = Integer.MAX_VALUE;
        int max = 0;
        int len = prices.length;
        for(int i = 0; i<len;i++) {
            if(prices[i]<min) {
                min = prices[i];
            }else {
                max = Math.max(max, prices[i] - min);
            }
        }
        return max;
        //O(N)
	}
}

