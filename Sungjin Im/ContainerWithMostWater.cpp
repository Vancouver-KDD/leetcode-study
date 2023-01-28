// Container With Most Water
// :author: SJ
// :date: Jan 27 2023
//
// You are given an integer array height of length n.
// There are n vertical lines drawn 
//      such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
//
// Find two lines that together with the x-axis form a container,
//      such that the container contains the most water.
//
// Return the maximum amount of water a container can store.
//
// Notice that you may not slant the container.
//
// Example 1:
// Input: height = [1,8,6,2,5,4,8,3,7]
// Output: 49
// Explanation : The above vertical lines are represented
//                  by array[1, 8, 6, 2, 5, 4, 8, 3, 7].In this case,
//                  the max area of water(blue section) the container can contain is 49.
//
// Example 2:
// Input: height = [1, 1]
// Output : 1
//

#include <iostream>
#include <vector>

using namespace std;

int maxArea(vector<int>& height) {
    int h = 0;
    int water = 0;

    int i = 0;
    int j = height.size() - 1;

    while (i < j) {
        int h = min(height[i], height[j]);
        water = max(water, (j - i) * h);

        while (height[i] <= h && i < j) {
            i++;
        }
            
        while (height[j] <= h && i < j) {
            j--;
        }
    }

    return water;
}

int main()
{
    vector<int> nums = { 1,8,6,2,5,4,8,3,7 };
//      vector<int> nums = { 1, 1 };
    int ans;

    ans = maxArea(nums);

    cout << ans << endl;
}