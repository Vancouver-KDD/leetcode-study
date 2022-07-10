#include "common.h"

int find(int* nums, int begin, int end){
    int incl = 0, excl = 0, temp = 0;
    if (begin > end) return 0;

    for (int i = begin; i <= end; i++){
        temp = incl;
        incl = excl + nums[i];
        excl = temp > excl ? temp : excl;
        printf("i = %d ---> temp = %d  |  incl = %d  |  excl = %d\n", i , temp, incl, excl);
    }

    return incl > excl ? incl: excl;
}

int rob(int* nums, int numsSize) {
    if (numsSize == 1) return nums[0];
    printf("first\n\n");
    int first = find(nums, 0, numsSize - 2);
    printf("\n\nlast\n");
    int last = find(nums, 1, numsSize - 1);

    return first> last ? first: last;
}


int main() {
    int arr[6] = {1, 2, 3, 1, 4, 2};
    printf("\n\nresult = %d\n", rob(arr, 6));
}