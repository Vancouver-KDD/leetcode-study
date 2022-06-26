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


int search2(int* nums, int numsSize, int target) { // slightly better
    int left = 0;
    int right = numsSize-1;
    int mid;

    while (left <= right) {
        mid = (left + right) / 2 ;

        if(target == nums[mid])
            return mid;

        if(nums[left] <= nums[mid]) {  // left side
            if (target > nums[mid] || target < nums[left]) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        else { //right side
            if(target < nums[mid] || target > nums[right]) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
    }
    return -1;
}