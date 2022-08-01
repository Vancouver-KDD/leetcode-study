#include "common.h"

int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    int up = 0, down = matrixSize - 1, left = 0, right = matrixColSize[0] - 1;  //edge
    int *arr = (int*)malloc(matrixSize * matrixColSize[0] *sizeof(int));
    *returnSize = 0;

    while (1){
        if(left <= right){
            for(int i = left; i <= right; i++)  arr[(*returnSize)++] = matrix[up][i];
            up++;
        }
        else break;
        if(up <= down){
            for(int i = up; i <= down; i++)  arr[(*returnSize)++] = matrix[i][right];
            right--;
        }
        else  break;
        if(left <= right){
            for(int i = right; i >= left; i--)  arr[(*returnSize)++] = matrix[down][i];
            down--;
        }
        else  break;
        if(up <= down){
            for(int i = down; i >= up; i--)  arr[(*returnSize)++] = matrix[i][left];
            left++;
        }
        else  break;
    }
    return arr;
}
