#include "common.h"


int maxProduct2(int* nums, int numsSize) {  // slight improvement
    int max = -1000;
    int front = 1;
    int rear = 1;
    int i, temp;
    for (i = 0; i < numsSize; ++i) {
        if (front == 0) front = 1; //if element == 0, array is divided, reset the product = 0.
        if (rear == 0) rear = 1;
        front *= nums[i];
        rear *= nums[numsSize - 1 - i];
        temp = front > rear ? front : rear;
        max = temp > max ? temp : max;
    }
    return max;
}

int maxProduct1(int* nums, int numsSize) {
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