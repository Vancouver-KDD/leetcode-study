#include "common.h"

int lengthOfLIS(int* nums, int numsSize){
    if(numsSize == 0) return 0;

    int* arr = (int*)malloc(sizeof(int) * numsSize);
    arr[0] = nums[0];
    int temp = 0;
    for(int i = 1; i < numsSize; i++) {
        if(nums[i] > arr[temp]) {
            arr[temp+1] = nums[i];
            temp++;
        }
        else {
            for(int j = 0; j <= temp; j++) {
                if(arr[j] >= nums[i]) {
                    arr[j] = nums[i];
                    break;
                }
            }
        }
    }

    return temp + 1;
}


int lengthOfLIS2(int* nums, int numsSize)
{
    int *arr = malloc(sizeof(int) * numsSize);

    int temp;
    for (int i = 0; i < numsSize; i++) {
        arr[i] = 1;

        for (int j = 0; j < i; j++) {
            if (nums[i] > nums[j]) {
                temp = 1 + arr[j];
                if (temp > arr[i]) arr[i] = temp;
            }
        }
    }

    int max = 0;
    for (int i = 0; i < numsSize; i++)
        if (arr[i] > max)
            max = arr[i];
    return max;
}
