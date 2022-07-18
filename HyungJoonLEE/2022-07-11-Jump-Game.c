#include "common.h"

bool canJump(int* nums, int numsSize){
    int temp = 0;
    for(int i = 0; i < numsSize; i++){
        if (temp < i) return false;
        temp = temp > i + nums[i] ? temp : i + nums[i];
    }
    return true;
}
