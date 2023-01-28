// Longest Consecutive Sequence
// :author: SJ
// :date: Jan 27 2023
//
// Given an unsorted array of integers nums,
// return the length of the longest consecutive elements sequence.
// 
// You must write an algorithm that runs in O(n) time.
//
// Example 1:
// Input: nums = [100, 4, 200, 1, 3, 2]
// Output : 4
// Explanation : The longest consecutive elements sequence is[1, 2, 3, 4].Therefore its length is 4.
// 
// Example 2 :
//
// Input : nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
// Output : 9
//


#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;


int longestConsecutive(vector<int>& nums) {
    unordered_set<int> s(nums.begin(), nums.end());

    int longest_sequence = 0;

    for (int i = 0; i < nums.size(); i++)
    {
        if (s.find(nums[i] - 1) != s.end())
            continue;

        else
        {
            int count = 0;
            int current_element = nums[i];

            while (s.find(current_element) != s.end())
            {
                count++;
                current_element++;
            }

            longest_sequence = max(longest_sequence, count);
        }
    }

    return longest_sequence;
}


int main()
{
    //    vector<int> nums = { 100, 4, 200, 1, 3, 2 };
    vector<int> nums = { 0, 3, 7, 2, 5, 8, 4, 6, 0, 1 };

    int ans = 0;


    ans = longestConsecutive(nums);
    cout << ans << endl;

    return 0;
}
