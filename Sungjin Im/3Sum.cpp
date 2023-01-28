// 3 Sum
// :author: SJ
// :date: Jan 27 2023
//
// Given an integer array nums, 
// return all the triplets [nums[i], nums[j], nums[k]] 
// such that i != j, i != k, and j != k, 
// and nums[i] + nums[j] + nums[k] == 0.
//
// Notice that the solution set must not contain duplicate triplets.
//
// Example 1:
// Input: nums = [-1, 0, 1, 2, -1, -4]
// Output : [[-1, -1, 2], [-1, 0, 1]]
// Explanation :
//    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
//    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
//    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
//    The distinct triplets are[-1, 0, 1] and [-1, -1, 2].
//    Notice that the order of the output and the order of the triplets does not matter.
// 
// Example 2:
// Input: nums = [0, 1, 1]
// Output : []
// Explanation : The only possible triplet does not sum up to 0.
// 
// Example 3 :
// Input : nums = [0, 0, 0]
// Output : [[0, 0, 0]]
// Explanation : The only possible triplet sums up to 0.
//




#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


vector<vector<int>> threeSum(vector<int>& nums) {
    sort(nums.begin(), nums.end());    //Sorted Array
    if (nums.size() < 3) {    //Base case 1
        return {};
    }
    if (nums[0] > 0) {        //Base case 2
        return {};
    }
    vector<vector<int>> answer;
    for (int i = 0; i < nums.size(); ++i) {     //Traversing the array to fix the number.
        if (nums[i] > 0) {     //If number fixed is +ve, stop there because we can't make it zero by searching after it.
            break;
        }
        if (i > 0 && nums[i] == nums[i - 1]) {    //If number is getting repeated, ignore the lower loop and continue.
            continue;
        }
        int low = i + 1, high = nums.size() - 1;   //Make two pointers high and low, and initialize sum as 0.
        int sum = 0;
        while (low < high) {                          //Search between two pointers, just similiar to binary search.
            sum = nums[i] + nums[low] + nums[high];
            if (sum > 0) {   //If sum is +ve, means, we need more -ve numbers to make it 0, decreament high (high--).
                high--;
            }
            else if (sum < 0) { //If sum is -ve, means, we need more +ve numbers to make it 0, increament low (low++).
                low++;
            }
            else {
                answer.push_back({ nums[i] , nums[low] , nums[high] });  //we have found the required triplet, push it in answer vector
                int last_low_occurence = nums[low], last_high_occurence = nums[high];  //Now again, to avoid duplicate triplets, we have to navigate to last occurences of num[low] and num[high] respectively
                while (low < high && nums[low] == last_low_occurence) {   // Update the low and high with last occurences of low and high.
                    low++;
                }
                while (low < high && nums[high] == last_high_occurence) {
                    high--;
                }
            }
        }
    }
    return answer;      //Return the answer vector.
}


int main()
{
    vector<int> nums = { -1, 0, 1, 2, -1, -4 };
    vector<vector<int>> ans;

    ans = threeSum(nums);

    for (vector<vector<int>>::iterator it = ans.begin(); it != ans.end(); ++it) {
        for (vector<int>::iterator it2 = it->begin(); it2 != it->end(); ++it2) {
            cout << *it2 << " ";
        }
        cout << endl;
    }
}
