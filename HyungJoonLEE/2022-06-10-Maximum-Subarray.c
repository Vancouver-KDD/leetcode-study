#include "common.h"


int maxSubArray(int* nums, int numsSize);
int maxSubArray2(int* nums, int numsSize);

int main() {
    int num[10] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    maxSubArray(num, 10);

}


int maxSubArray(int* nums, int numsSize) {

    if(numsSize == 1) return nums[0];

    int temp = nums[0];
    int sum = nums[0];

    for(int i = 1; i < numsSize; i++) {
        printf("nums[%d] = %d\n", i, nums[i]);
        temp += nums[i];
        printf("temp = %d\n", temp);

        if(temp < nums[i]) {
            temp = nums[i];
            printf("===> temp = %d\n\n", temp);
        }
        else {
            printf("temp > nums[%d]\n\n", i);
        }

        if(temp > sum) {
            printf("sum = %d\n", sum);
            printf("temp > sum\n");
            sum = temp;
            printf("RESET sum = %d\n\n", sum);
        }
    }
    return sum;
}


int maxSubArray2(int* nums, int numsSize) {

    for(int i = 1; i < numsSize; i++) {
        if(nums[i - 1] > 0) {
            nums[i] += nums[i - 1];
        }
    }

    int sum = nums[0];
    for(int j = 1; j < numsSize; j++){
        if(nums[j] > sum){
            sum = nums[j];
        }
    }
    return sum;
}