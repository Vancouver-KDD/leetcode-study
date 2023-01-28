// Product of Array Except Self
// :author: SJ
// :date: Jan 27 2023
//
// Given an integer array nums, 
// return an array answer 
// such that answer[i] is equal 
// to the product of all the elements of nums 
// except nums[i].
// 
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
//
// You must write an algorithm that runs in O(n) time 
// and without using the division operation.
//
// Example 1:
// Input: nums = [1, 2, 3, 4]
// Output : [24, 12, 8, 6]
// 
// Example 2 :
// Input : nums = [-1, 1, 0, -3, 3]
// Output : [0, 0, 9, 0, 0]
//


#include <iostream>
#include <vector>

using namespace std;

vector<int> product_except_self(vector<int>& nums)
{
    int n = nums.size();

    vector<int> ans(n);

    ans[n - 1] = 1; // ans array used as right product array

    for (int i = n - 2; i >= 0; i--) {
        ans[i] = nums[i + 1] * ans[i + 1];
    }

    int leftProd = 1;
    for (int i = 0; i < n; i++) {
        ans[i] = leftProd * ans[i];
        leftProd = leftProd * nums[i];
    }

    return ans;
}


int main()
{
    //    vector<int> nums = { 1, 2, 3, 4 };
    vector<int> nums = { -1, 1, 0, -3, 3 };
    vector<int> ans = product_except_self(nums);

    for (const int& a : ans) {
        cout << a << " ";
    }
    cout << endl;

    return 0;
}
