/**
 * @param {number[]} prices
 * @return {number}
 */
// reference: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/3335782/easy-and-fast-99-beats/?languageTags=javascript
var maxProfit = function(prices) {
    if (!prices || prices.length < 1) return 0
    
    let lowest = prices[0]
    let result = 0
    // loop through all items in prices array
    for (const item of prices) {
        // if item is lower than lowest, assign item to lowest
        if (item < lowest) lowest = item
        // if current item is bigger than lowest 
        // and current item - lowest is bigger than the result
        // assign new result of current item - lowest
        else if (result < item - lowest) result = item - lowest
        // if current item - lowest is smaller than the result
        // it just goes to next item in the array
    }
    return result

    // complexity
    // time: O(n)
    // space: O(1)
};

var maxProfit2 = function(prices) {
    // check if parameter is valid
    if (!prices || prices.length < 1) return 0
    
    // find lowest number
    let lowest = prices[0]
    for (const item of prices) {
    	if (item < lowest) lowest = item
    }
    
    // find highest number after lowest number
    let highest = lowest
    for (let i = prices.indexOf(lowest); i < prices.length; i++) {
        if (prices[i] > highest) highest = prices[i]
    }
    
    // if there was no bigger number after lowest return 0
    if (lowest === highest) return 0
    
    // else return the result
    return highest - lowest

    // PROBLEM: the problem of this solution is that, 
    // if the input is [2,4,1], it can't find 2 & 4 since lowest number is 1.
    
    // complexity
    // time: O(n)
    // space: O(1)
};