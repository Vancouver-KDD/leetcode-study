// Contains Duplicate
// :author: SJ
// :date: Jan 27 2023
//
// Given an integer array nums,
// return true
//      if any value appears at least twice in the array,
// 
// and return false
//      if every element is distinct.
//
// Example 1:
// Input: nums = [1, 2, 3, 1]
// Output : true
//
// Example 2 :
// Input : nums = [1, 2, 3, 4]
// Output : false
//
// Example 3 :
// Input : nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
// Output : true
//

#include <iostream>
#include <vector>
#include <map>

using namespace std;

bool containsDuplicate(vector<int>& nums) {
    map<int, int> mp;
    bool flag = false;

    for (auto i : nums) {
        mp[i]++;
    }

    for (auto i : mp) {
        if (i.second >= 2) {
            return true;
        }
    }

    return flag;
}

int main()
{
    vector<int> nums = { 1, 2, 3, 1 };
    //vector<int> nums = { 1, 2, 3, 4 };
    //vector<int> nums = { 1, 1, 1, 3, 3, 4, 3, 2, 4, 2 };

    bool ans = containsDuplicate(nums);

    if (ans) {
        cout << "true" << endl;
    }
    else {
        cout << "false" << endl;
    }

    return 0;
}
