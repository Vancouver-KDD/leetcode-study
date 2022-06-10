#include "common.h"


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int *result = (int *)malloc(sizeof(int) * numsSize);
    if (!result) {
        printf("Memory allocation failed\n");
        return;
    }

    result[0] = 1;

    for (int i = 1; i < numsSize; i++) {
        result[i] = result[i - 1] * nums[i - 1];
    }

    int tmp = 1;
    for(int i = numsSize - 1; i >= 0; i--) {
        result[i] = result[i] * tmp;
        tmp = tmp * nums[i];
    }

    *returnSize = numsSize;
    return result;
}



//TODO: Using linked list?
struct node {
    int val;
    int index;
    struct node *next;
};

void add(struct node *target, int data, int seq) {
    struct node *newNode = malloc(sizeof(struct node));
    newNode->next = target->next;
    newNode->val = data;
    newNode->index = seq;
    target->next = newNode;
}
