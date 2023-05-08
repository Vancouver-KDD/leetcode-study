var maxProfit = function (prices) {
  let maxProfit = 0;
  let buyPrice = prices[0];

  for (let sell = 1; sell < prices.length; sell++) {
    let sellPrice = prices[sell];
    let profit = sellPrice - buyPrice;
    maxProfit = Math.max(maxProfit, profit);

    if (sellPrice < buyPrice) buyPrice = sellPrice;
  }

  return maxProfit;
};
