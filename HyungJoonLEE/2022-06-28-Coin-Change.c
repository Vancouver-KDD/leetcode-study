#include "common.h"


int coinChange(int* coins, int coinsSize, int amount){
    int* arr = (int*)malloc(sizeof(int) * (amount + 1));
    memset(arr, -1, sizeof(int) * (amount + 1));
    arr[0] = 0;

    for(int i = 1; i < amount + 1; ++i) {
        for(int j = 0; j < coinsSize; ++j) {
            if(i - coins[j] >= 0 && arr[i-coins[j]] != -1) {
                if(arr[i] == -1 || arr[i] > arr[i-coins[j]] + 1) {
                    arr[i] = arr[i - coins[j]] + 1;
                }
            }
        }
    }

    return arr[amount];
}