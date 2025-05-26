/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  let minPrice = prices[0];
  let result = 0;
  for (let price of prices) {
    minPrice = Math.min(price, minPrice);
    const currentProfit = price - minPrice;
    result = Math.max(result, currentProfit);
  }
  return result;
};
