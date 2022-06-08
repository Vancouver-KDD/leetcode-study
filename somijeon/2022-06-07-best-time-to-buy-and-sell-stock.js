// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// Return the maximum profit you can achieve from this transaction.

//* Example 1:

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

//? If you cannot achieve any profit, return 0.

//* Example 2:

// Input: prices = [7,6,4,3,1]
// Output: 0

const maxProfit = function (prices) {
  let l = 0;
  let r = 1;
  let maxP = 0;
  while (r < prices.length) {
    if (prices[l] < prices[r]) {
      let profit = prices[r] - prices[l];
      maxP = Math.max(maxP, profit);
      r += 1;
    } else {
      l = r;
      r += 1;
    }
  }
  return maxP;
};

//* another way
// const maxProfit = function (prices) {
//   let profit;
//   let maxProfit = 0;

//   prices.forEach(function (buy, index) {
//     let rest = prices.slice(index + 1);
//     if (rest) {
//       let sell = Math.max(...rest);
//       sell > buy ? (profit = sell - buy) : null;
//       profit > maxProfit ? (maxProfit = profit) : null;
//     }
//   });
//   return maxProfit;
// };
