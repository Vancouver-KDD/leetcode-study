/**
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
 */

// first solution - 2 pointers
var maxProfit = function (prices) {
  let profit = 0;
  let left = 0;
  let right = 1;

  //buy low sell high
  while (right < prices.length) {
    // if profitable
    if (prices[left] < prices[right]) {
      let currProfit = prices[right] - prices[left];
      profit = Math.max(currProfit, profit);
    } else {
      // if left price is bigger than right price, move left pointer to right
      // since we only want to buy at lowest price
      left = right;
    }
    // move right pointer to next day to check if its profitable
    right++;
  }
  return profit;
  //test
};
