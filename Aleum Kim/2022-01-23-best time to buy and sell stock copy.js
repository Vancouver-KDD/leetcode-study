// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

function maxProfit(prices) {

    let buy = prices[0]
    prices[0] = 0;
    let profit = 0;
    for(let i = 1; i< prices.length; i++) {
        if(buy > prices[i]) {
            buy = prices[i]
            prices[i] = 0;
        } else {
            profit = Math.max(prices[i].buy,profit)
        }
    }
}