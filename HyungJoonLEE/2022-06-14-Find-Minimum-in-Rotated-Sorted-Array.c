#include "common.h"

int findMin(int* nums, int numsSize){
    int left = 0, right = numsSize - 1;
    while (left < right) {
        int mid = (left + right) / 2;
        if (nums[mid] < nums[right])
            right = mid;
        else if (nums[mid] > nums[left])
            left = mid + 1;
    }
    return nums[left];
}

int main() {
    int nums[7] = {4,5,6,7,0,1,2};
    findMin(nums, 7);
    return 0;
}