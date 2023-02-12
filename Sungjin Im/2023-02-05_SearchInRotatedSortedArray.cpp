// SearchInRotatedSortedArray.cpp : This file contains the 'main' function. Program execution begins and ends there.
// :author: SJ
// :date: Feb 05 2023
//
// There is an integer array nums sorted in ascending order (with distinct values).
// Prior to being passed to your function, 
// nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
// such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
//
// For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
// 
// Given the array nums after the possible rotationand an integer target,
// return the index of target if it is in nums, or -1 if it is not in nums.
// You must write an algorithm with O(log n) runtime complexity.
//
// Example 1:
// Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
// Output : 4
// 
// Example 2 :
// Input : nums = [4, 5, 6, 7, 0, 1, 2], target = 3
// Output : -1
//
// Example 3 :
// Input : nums = [1], target = 0
// Output : -1
//


#include <iostream>
#include <vector>

using namespace std;

int FindIndex(vector<int> nums, int target)
{
    int beg = 0;
    int end = nums.size() - 1;
    int mid = 0;

    while (beg <= end)
    {
        mid = (beg + end) / 2;

        if (nums[mid] == target)
        {
            return mid;
        }

        if (nums[beg] <= nums[mid])
        {
            if (target <= nums[mid] && target >= nums[beg])
            {
                end = mid - 1;
            }
            else
            {
                beg = mid + 1;
            }
        }
        else
        {
            if (target >= nums[mid] && target <= nums[end])
            {
                beg = mid + 1;
            }
            else
            {
                end = mid - 1;
            }
        }
    }

    return -1;
}

int main()
{
    vector<int> nums = { 4, 5, 6, 7, 0, 1, 2 };
    //vector<int> nums = { 1 };

    int target = 0;
    int ans = 0;

    ans = FindIndex(nums, target);

    cout << ans << endl;

    return 0;
}
