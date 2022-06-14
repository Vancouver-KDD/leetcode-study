#include "common.h"


int maxProduct(int* nums, int numsSize) {
    if(numsSize == 0 || !nums) return 0;
    if(numsSize == 1) return *nums;

    int max = (nums[0] > 0) ? nums[0] : 0;
    int min = (nums[0] < 0) ? nums[0] : 0;
    int result = max;
    int tmp = 0;

    for(int i = 1; i < numsSize; i++) {
        if(nums[i] > 0) {
            max = (max == 0) ? nums[i] : max * nums[i];
            min *= nums[i];
        }
        else if (nums[i] < 0) {
            tmp = max;
            max = min * nums[i];
            min = (tmp == 0) ? nums[i] : tmp*nums[i];
        }
        else max = min = 0;

        result = (result >= max) ? result : max;
    }
    return result;
}