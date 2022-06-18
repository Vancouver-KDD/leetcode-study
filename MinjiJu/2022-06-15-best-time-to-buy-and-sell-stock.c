int maxProfit(int* prices, int pricesSize){
    
    int profit = 0;
    int minprice = prices[0];
    
    if(pricesSize<2) { return 0; }
    
    for(int i=1; i<pricesSize; i++){

        if(prices[i]<prices[i-1]){
            // update min price
            minprice = fmin(minprice,prices[i]);
        } else {
            // update max profit
            profit = fmax(profit, prices[i]-minprice);
        }
    }
    return profit;
}