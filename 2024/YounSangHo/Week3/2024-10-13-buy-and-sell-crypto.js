class Solution {
  /**
   * @param {number[]} prices
   * @return {number}
   */
  maxProfit(prices) {
    // prices in ith day
    // buy in a single day
    // sell in a different day in the future
    // You have to make the maximum profit you can achieve.
    // You may choose to not make any transactions then you return 0

    // 10, 1, 5, 6, 7, 1
    // 1. 가장 작은 가격을 찾는다
    // 2. 가장 작은 값보다 값이 큰 경우 값을 비교하여 이익 값을 낸다.
    // 3. 이익 값이 기존에 넣었던 이익 값보다 큰 경우 값을 바꾼다.
    let minPrice = prices[0];
    let result = 0;

    prices.forEach((price) => {
      if (minPrice >= price) {
        minPrice = price;
      } else {
        result = Math.max(result, price - minPrice);
      }
    });

    return result;
  }
}
