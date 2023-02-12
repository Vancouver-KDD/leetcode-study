// Top K Frequent Elements
// :author: SJ
// :date: Jan 26 2023
// 
// Given an integer array nums and an integer k,
// return the k most frequent elements.
// 
// You may return the answer in any order.
// 
// Example 1:
// Input: nums = [1, 1, 1, 2, 2, 3], k = 2
// Output : [1, 2]
// 
// Example 2 :
// Input : nums = [1], k = 1
// Output : [1]
//

#include <iostream>
#include <vector>
#include <map>

using namespace::std;


vector<int> top_k_frequent_elements(vector<int>& nums, int k) {
    vector<int> result;
    map<int, int> m;
    multimap<int, int, greater<int>> multi_m;

    for (const int& i : nums) {
        auto it = m.find(i);

        if (it != m.end()) {
            it->second++;
        }
        else {
            m.insert({ i, 1 });
        }
    }



    for (auto& it : m) {
        multi_m.insert(make_pair(it.second, it.first));
    }


    //for (auto& it : m) {
    //    cout << it.first << " " << it.second << "\n";
    //}

    //cout << endl;

    //for (auto& it : multi_m) {
    //    cout << it.first << " " << it.second << "\n";
    //}

    int count = 0;

    for (auto& it : multi_m) {
        count++;
        if (count > k) {
            return result;
        }
        result.push_back(it.second);
    }

    return result;
}

int main()
{
    vector<int> nums = { 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3 };
    int k = 2;

    //vector<int> nums = { 1, 1, 1, 2, 2, 3 };
    //int k = 2;

    //vector<int> nums = { 1 };
    //int k = 1;




    vector<int> result;


    result = top_k_frequent_elements(nums, k);


    for (const int& r : result) {
        cout << r << " ";
    }
    cout << endl;

    return 0;
}
