// TwoSum.cpp : This file contains the 'main' function. Program execution begins and ends there.
// :author: SJ
// :date: Jan 17 2023
//
// Given an array of integers nums and an integer target,
// return indices of the two numbers such that they add up to target.
//
// You may assume that each input would have exactly one solution,
// and you may not use the same element twice.
//
// You can return the answer in any order.
//
// Example 1:
// Input: nums = [2, 7, 11, 15], target = 9
// Output : [0, 1]
// Explanation : Because nums[0] + nums[1] == 9, we return[0, 1].
//
// Example 2 :
// Input : nums = [3, 2, 4], target = 6
// Output : [1, 2]
//
// Example 3 :
// Input : nums = [3, 3], target = 6
// Output : [0, 1]
//


#include <iostream>

using namespace std;

void two_sum(int count, int* arr, int t_num, int* r_arr)
{
    int sum = 0;

    for (int i = 0; i < count - 1; i++) {
        for (int j = i + 1; j < count; j++) {
            if (arr[i] + arr[j] == t_num) {
                r_arr[0] = i;
                r_arr[1] = j;
                return;
            }
        }
    }
}


int main()
{
    int ex_num = 1;
    int arr_count = 0;
    int arr[10] = { 0 };
    int t_num = 9;
    int index = 0;

    switch (ex_num)
    {
    case 1:
        arr_count = 4;
        index = 0;
        arr[index] = 2;     index++;
        arr[index] = 7;     index++;
        arr[index] = 11;    index++;
        arr[index] = 15;    index++;
        t_num = 9;
        break;

    case 2:
        arr_count = 3;
        index = 0;
        arr[index] = 3;     index++;
        arr[index] = 2;     index++;
        arr[index] = 4;     index++;
        t_num = 6;
        break;

    case 3:
        arr_count = 2;
        index = 0;
        arr[index] = 3;     index++;
        arr[index] = 3;     index++;
        t_num = 6;
        break;

    default:
        cout << "Not the test case number. Try again." << endl;
        break;
    }


    int result_arr[2] = { -1, -1 };

    two_sum(arr_count, arr, t_num, result_arr);

    cout << "[" << result_arr[0] << ", " << result_arr[1] << "]";
    cout << endl;
}
