#include "common.h"

int maxSubArray(int* nums, int numsSize){

    if(numsSize == 1) return nums[0];

    int temp = nums[0];
    int sum = nums[0];

    for(int i = 1; i < numsSize; i++) {
        temp += nums[i];

        if(temp < nums[i]) {
            temp = nums[i];
        }

        if(temp > sum) {
            sum = temp;
        }
    }
    return sum;
}