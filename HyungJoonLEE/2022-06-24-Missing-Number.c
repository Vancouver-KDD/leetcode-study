#include "common.h"

int compare(int *a, int *b) {
    return *(int *)a - *(int *)b;
}

int missingNumber(int* nums, int numsSize) {
    int index = 0;
    int *arr = malloc(sizeof(int) * (numsSize+1));
    memset(arr, 0, sizeof(int) * (numsSize+1));

    for (int i = 0; i < numsSize; i++) {
        arr[nums[i]] = nums[i];
    }

    for (int i = 1; i <= numsSize; i++) {
        if(arr[i] - arr[i - 1] != 1) {
            index = i;
            break;
        }
    }
    return index;
}
