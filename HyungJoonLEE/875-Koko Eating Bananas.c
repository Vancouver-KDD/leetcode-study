#include "common.h"

bool isSmall (int *piles, int pilesSize, int k, int h) {
    int sum = 0;
    for (int i = 0; i < pilesSize; i++)
        sum += piles[i] / k + ((piles[i] % k) > 0 ? 1 : 0);

    return sum > h;
}

int minEatingSpeed(int* piles, int pilesSize, int h){
    int max = 0;
    for (int i = 0; i < pilesSize; ++i) {
        max = piles[i] > max ? piles[i] : max;
    }

    int low = 1, high = max;

    while (low < high) {
        int mid = (low + high) / 2;

        if (isSmall(piles, pilesSize, mid, h))
            low = mid + 1;
        else
            high = mid;
    }

    return low;
}