/**
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 * You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
 * Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 */

// 1. keeping track of the min cost found so far
// and calculate the profit for each day updating current profit (greatest)
class Solution {
	public static int maxProfit(int[] prices) {
		int curProfit = 0;
        int minCost = 10000; // 0 <= prices[i] <= 10^4
		for(int i = 0; i < prices.length; i++) {
			if (prices[i] < minCost) {
				minCost = prices[i];
			}
			int dif = prices[i] - minCost;
			
			if(dif > curProfit) curProfit = dif;
		}
		return curProfit;
	}
}