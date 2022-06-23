#include "common.h"

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
    int count = 0;
    for (int i = 0; i <= n; i++) {
        result[i] = helper(i);
    }

    return result;
}
