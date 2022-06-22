#include "common.h"
#include <math.h>


int maxArea1(int* height, int heightSize){
    int left =0, right = heightSize-1;
    int max = 0;

    while(left < right){
        int temp_height = height[left] < height[right] ? height[left] : height[right];

        if(max < temp_height * (right-left)) {
            max = temp_height * (right - left);
        }
        height[left] < height[right] ? left++ : right--;
    }

    return max;
}


int maxArea2(int* height, int heightSize)
{
    int i = 0, j = heightSize - 1;
    int max = 0;

    while (i < j) {
        int curr_cap = (j - i) * (int)fmin(height[i], height[j]);
        max = (int)fmax(max, curr_cap);

        if (height[i] > height[j])
            j--;
        else
            i++;
    }
    return max;
}