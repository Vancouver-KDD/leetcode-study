#include "common.h"

int search(int* nums, int numsSize, int target){
    int left = 0;
    int right = numsSize - 1;
    while (left < right) {
        int mid = (left + right) / 2;
        if (target > nums[right])
            if (nums[mid] < target && nums[mid] > nums[right]) left = mid + 1;
            else right = mid;
        else
        if (nums[mid] >= target && nums[mid] <= nums[right]) right = mid;
        else left = mid + 1;
    }
    return nums[left] == target ? left : -1;
}