#include "common.h"

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int rob(int* nums, int numsSize) {

    int *arr = malloc(sizeof(int) * numsSize);

    if (numsSize == 0) return 0;
    else {
        for (int i = 0; i < numsSize; i++) {
            switch (i) {
                case 0:
                    arr[i] = nums[0];
                    break;
                case 1:
                    arr[i] = MAX(nums[i], arr[i - 1]);
                    break;
                default:
                    arr[i] = MAX(nums[i] + arr[i - 2], arr[i - 1]);
            }
        }
    }

    return arr[numsSize - 1];
}