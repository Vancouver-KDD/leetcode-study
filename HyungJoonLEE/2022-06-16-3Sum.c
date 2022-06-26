#include "common.h"

int compare(const int* a, const int* b){
    return (*a - *b);
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){
    *returnSize = 0;
    *returnColumnSizes = (int*)malloc(numsSize * numsSize * sizeof(int));
    int ** result = (int**)malloc(numsSize * numsSize * sizeof(int*));// malloc array initial, just set one array size
    if(numsSize<3) return result;

    qsort(nums, numsSize, sizeof(int), compare);
    int i = 0, j, k;

    while(i<numsSize-2) {
        if(i != 0 && nums[i] == nums[i-1]) {
            i++;
            continue;
        }
        j = i + 1;
        k = numsSize - 1;

        while(j < k) {
            if((nums[i] + nums[j] + nums[k]) == 0) {
                if(*returnSize!=0) {
                    if(nums[i] == result[*returnSize-1][0] && nums[j] == result[*returnSize-1][1]) {
                        j++;
                        continue;
                    }
                }
                (*returnColumnSizes)[*returnSize] = 3;
                result[*returnSize] = malloc(sizeof(int) * 3);
                result[*returnSize][0] = nums[i];
                result[*returnSize][1] = nums[j];
                result[*returnSize][2] = nums[k];
                *returnSize +=  1;
                j++;
                k--;
            }
            else if((nums[i] + nums[j] + nums[k]) < 0) j++;
            else if((nums[i] + nums[j] + nums[k]) > 0) k--;
        }
        i++;
    }
    return result;
}