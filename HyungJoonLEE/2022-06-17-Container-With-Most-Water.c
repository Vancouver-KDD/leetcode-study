#include "common.h"
#include <math.h>


int maxArea1(int* height, int heightSize){
    int left =0, right = heightSize-1;
    int max = 0;

    while(left < right){
        int temp_height = height[left] < height[right] ? height[left] : height[right];

        if (max < temp_height * (right-left)) {
            max = temp_height * (right - left);
        }
        height[left] < height[right] ? left++ : right--;
    }

    return max;
}


int maxArea2(int* height, int heightSize) // improvements
{
    int left = 0, right = heightSize - 1;
    int max = 0;

    while (left < right) {
        int curr_cap = (right - left) * (int)fmin(height[right], height[left]);
        max = (int)fmax(max, curr_cap);

        if (height[left] > height[right])
            right--;
        else
            left++;
    }
    return max;
}

int maxArea3(int* height, int heightSize) { // My love Brute Force!!
    int max = 0;
    for(int i = 0; i < heightSize - 1; i++){
        for(int j = i + 1; j < heightSize; j++){
            int temp = (height[i] < height[j] ? height[i] : height[j]) *(j - i);
            max = max > temp ? max :temp;
        }
    }
    return max;
}