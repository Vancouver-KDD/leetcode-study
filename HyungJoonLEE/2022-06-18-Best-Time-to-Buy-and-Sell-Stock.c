#include "common.h"

int maxProfit(int* prices, int pricesSize){
    int min = prices[0];
    int max = 0;

    if( pricesSize == 0) return 0;

    for(int i = 0; i < pricesSize; i++){
        int profit = prices[i] - min;
        if(prices[i] < min) min = prices[i];
        if(profit > max) max = profit;
    }

    return max;
}
