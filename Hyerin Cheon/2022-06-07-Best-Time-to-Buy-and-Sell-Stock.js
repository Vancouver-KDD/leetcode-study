// 1. using two for loop 
// O(n^2)
var maxProfit = function(prices){
  let maxProfit = 0;  //when no profit is made
  for(let buyPrice = 0; buyPrice < prices.length; buyPrice++){
    for( let sellPrice = buyPrice + 1; sellPrice < prices.length; sellPrice++){
      let profit = prices[sellPrice] - prices[buyPrice]
      maxProfit = Math.max(maxProfit, profit)
    }
  }
  return maxProfit;
}

// 2. set minPrice and subtract from sellPrice, store the value as profit and compare with maxProfit
// O(n)
function maxProfit(prices){
  let maxProfit = 0; 
  let minPrice = prices[0]
  for(let sell = 1; sell < prices.length; sell++){
    let sellPrice = prices[sell]
    let profit = sellPrice - minPrice
    maxProfit = Math.max(maxProfit, profit)

    if(sellPrice < minPrice){
      minPrice = sellPrice
    }
  }
  return maxProfit
}
