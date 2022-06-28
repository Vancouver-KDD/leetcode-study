#include <stdio.h>

int findNum(int *arr, int arrSize, int target) {

    int left = 0, right = arrSize - 1;
    int mid = 0;

    while (left <= right) {
        mid = (left + right) / 2;

        if (target == arr[mid]) return mid;

        // left
        if (arr[left] <= arr[mid]) {
            if (target < arr[left] || target > arr[mid]) left = mid + 1;
            else right = mid - 1;
        }

            // right
        else
            if (target > arr[right] || target < arr[mid]) right = mid - 1;
            else left = mid + 1;
    }

    return -1;
}

int main() {
    int arr[7] = {4,5,6,7,0,1,2};
    printf("%d\n", findNum(arr, 7, 0));
    printf("%d\n", 0 / 2);
    return 0;
}