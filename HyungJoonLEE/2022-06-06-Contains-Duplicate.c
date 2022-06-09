#include "common.h"

#define BUCKET_COUNT 975012

bool containsDuplicateSelectionSort(int* nums, int numsSize);
bool containsDuplicateInsertionSort(int* nums, int numsSize);
bool containsDuplicateBubbleSort(int* nums, int numsSize);
bool containsDuplicateSequentialSort(int* nums, int numsSize);
bool containsDuplicateGeneral(int* nums, int numsSize);

int main() {
    int ex1[4] = {1,2,3,1};
    int ex2[4] = {1,2,3,4};
    int ex3[10] = {1,1,1,3,3,4,3,2,4,2};
    containsDuplicateSelectionSort(ex3, 10);
}

int hashing(int num) {
    return num % BUCKET_COUNT;
}

bool containsDuplicate(int* nums, int numsSize) {
    bool arr_positive[BUCKET_COUNT] = {false};
    bool arr_negative[BUCKET_COUNT] = {false};

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] < 0) {
            nums[i] = abs(nums[i]);
            if (arr_negative[hashing(nums[i])] == true) return true;
            arr_negative[hashing(nums[i])] = true;
        }
        else {
            if (arr_positive[hashing(nums[i])] == true) return true;
            arr_positive[hashing(nums[i])] = true;
        }
    }
    return false;
}

/**
 * Bad approach sequential sort
 * Time complexity = O(n^2)
 * Space complexity = ?
 * Result = Time Limit Exceeded
 */
bool containsDuplicateSequentialSort(int* nums, int numsSize) {
    int temp = 0;
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] > nums[j]) {
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] == nums[i + 1]) return true;
    }
    return false;
}


/**
 * Bad approach bubble sort
 * Time complexity = O(n^2)
 * Space complexity = ?
 * Result = Time Limit Exceeded
 */
bool containsDuplicateBubbleSort(int* nums, int numsSize) {
    int temp = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = 0; j < numsSize - 1 - i; j++) {
            if (nums[j] > nums[j + 1]) {
                temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            }
        }
    }
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] == nums[i + 1]) return true;
    }
    return false;
}


/**
 * Bad approach insertion sort
 * Time complexity = O(n^2)
 * Space complexity = O(1)
 * Result = Time Limit Exceeded
 */
//TODO: Need to see again
bool containsDuplicateInsertionSort(int* nums, int numsSize) {
    int temp, index = 0;
    for (int i = 1; i < numsSize; i++) {
        temp = nums[i];
        for (index = i - 1; index >= 0 && nums[index] > temp; index--) {
            if (nums[index] > temp) {
                nums[index + 1] = nums[index];
            }
            else break;
        }
    }
    nums[index + 1] = temp;
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] == nums[i + 1]) return true;
    }
    return false;
}


/**
 * Bad approach selection sort
 * Time complexity = O(n^2)
 * Space complexity = O(1)
 * Result = Time Limit Exceeded
 */
//TODO: Need to see again
bool containsDuplicateSelectionSort(int* nums, int numsSize) {
    int temp = 0;
    for (int i = 0; i < numsSize - 1; i++) { // 마지막 대상 비교 필요 X
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] > nums[j]) {
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] == nums[i + 1]) return true;
    }
    return false;
}


/**
 * Bad approach general
 * @Time complexity = O(n^2)
 * @Space complexity = ?
 * Result = Time Limit Exceeded
 */
bool containsDuplicateGeneral(int* nums, int numsSize) {
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] == nums[j]) {
                return true;
            }
        }
    }
    return false;
}