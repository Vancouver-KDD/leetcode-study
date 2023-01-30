class Solution {
    public int maxProfit(int[] prices) {

        int max = 0;
        int maxResult = 0;

        for(int i = prices.length -1;i >=0; i--){
            max = Math.max(max, prices[i]);
            maxResult = Math.max( maxResult, max - prices[i] );
        }

        return maxResult;
    }
}