
// 121. Best Time to Buy and Sell Stock
// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
// Approach 1 
var maxProfit = function(prices) {
    let maxProfit = 0; 
    let cheapestPrice = prices[0]; 
    
    for(let i=0; i<prices.length; i++){
        const price = prices[i]; 
        
        if(price < cheapestPrice) {
            cheapestPrice = price;
        }
        
        const currentProfit = price - cheapestPrice; 
        maxProfit = Math.max(currentProfit, maxProfit); 
    }
    return maxProfit;   
};


// Approach 2
const maxProfit = (prices) => {
    let left = 0;
    let right = 1;
    let max_profit = 0;
    
    while(right < prices.length) {
      if(prices[left] < prices[right]) {
        let profit = prices[right] - prices[left];
        max_profit = Math.max(max_profit, profit);
      }else{
        left = right;
      }
      right++;
    }
    
    return max_profit;
  }

// Time Complexty :  Now, it is quite obvious that the Time Complexity is linear as we can see that only one loop runs in our code. Hence, our Time Complexity is O(n).
// Space Complecity : O(1) No extra space is needed
