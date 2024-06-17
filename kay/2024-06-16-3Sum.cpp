#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <set>

using namespace std;

class Solution {
public:
    void twoSum(int target, vector<int>& nums, vector<vector<int>>& threeSumArr, int idx) {
        int left = idx + 1, right = nums.size() - 1;
        while (left < right) {
            if (nums[left] + nums[right] == target) {
                threeSumArr.push_back({ nums[left], -target, nums[right] });
                left++;
                while (left < right && nums[left] == nums[left - 1])
                    left++;
            }
            else if (nums[left] + nums[right] < target)
                left++;
            else
                right--;
        }
    }
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> threeSumArr;
        set<int> numSet;
        for (auto num : nums) {
            numSet.insert(num);
        }
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() && nums[i] <= 0; i++) {
            int target = -nums[i];
            if (i == 0 || nums[i - 1] != nums[i])
                twoSum(target, nums, threeSumArr, i);
        }
        return threeSumArr;
    }
};

/*class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size() && nums[i] <= 0; i++) {
            if (i == 0 || nums[i-1] != nums[i])
                twoSum(nums, i, -nums[i], ans);
        }

        return ans;
    }

    void twoSum(vector<int>& nums, int idx, int target, vector<vector<int>>& ans) {
        int left = idx+1, right = nums.size() - 1;
        while (left < right) {
           // printf("%d %d %d\n",nums[left], nums[right], target);
            if (nums[left] + nums[right] < target)
                left++;
            else if (nums[left] + nums[right] > target)
                right--;
            else {
                vector<int> res;
                res.push_back(nums[idx]);
                res.push_back(nums[left++]);
                res.push_back(nums[right]);
                while (left<right && nums[left-1] == nums[left])
                    left++;
                ans.push_back(res);
            }
        }
        printf("\n");
    }
};*/