#include "common.h"

int bisearch(int* arr, int arrSize, int target) {
    int low, high, mid;

    low = 0;
    high = arrSize - 1;
    while (low <= high) {
        mid = (low + high) / 2;
        if (target == arr[mid]) return mid;
        else if (target < arr[mid]) high = mid - 1;
        else if (target > arr[mid]) low = mid + 1;
    }
    return -1;
}

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    for (int i = 0; i < matrixSize; i++) {
        if (bisearch(matrix[i], *matrixColSize, target) != -1) return true;
    }
    return false;
}