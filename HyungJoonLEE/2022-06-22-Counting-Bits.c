#include "common.h"



int* countBits2(int n, int* returnSize) {
    *returnSize = n + 1;

    int* result = malloc(sizeof(int) * (*returnSize));
    result[0] = 0;

    for(int i = 1; i <= n; i++) {
        result[i] = (i & 1) ? result[i >> 1] + 1 : result[i >> 1];
    }
    return result;
}


int helper(int num) {
    int count = 0;

    while(num != 0) {
        if ((num & 1) == 1) count ++;
        num >>= 1;
    }

    return count;
}


int* countBits(int n, int* returnSize) {
    *returnSize = n + 1;
    int *result = malloc(sizeof(int) * (*returnSize));

    for (int i = 0; i <= n; i++) {
        result[i] = helper(i);
    }

    return result;
}
