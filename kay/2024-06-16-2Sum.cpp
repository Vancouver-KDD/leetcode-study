#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {

public:
    vector<int> twoSum(vector<int> nums, int target) {
        unordered_map<int, int> numIdxMap;
        for (int i = 0; i < nums.size(); i++) {
            if (numIdxMap.find(target - nums[i]) != numIdxMap.end()) {
                return { numIdxMap[target - nums[i]], i };
            }
            numIdxMap[nums[i]] = i;
        }
        return vector<int>();
    }
};
/*
class Solution {
private:
struct Point{
    int val;
    int idx;
};
static bool cmp (Point &a, Point &b) {
    return a.val < b.val;
}
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<Point> valWithIdxArr;
        for (int i = 0 ; i < nums.size(); i++) {
            valWithIdxArr.push_back({nums[i], i});
        }
        sort(valWithIdxArr.begin(), valWithIdxArr.end(), cmp);
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            if (valWithIdxArr[left].val + valWithIdxArr[right].val == target) {
                return {valWithIdxArr[left].idx, valWithIdxArr[right].idx};
            }
            else if (valWithIdxArr[left].val + valWithIdxArr[right].val > target)
                right--;
            else if (valWithIdxArr[left].val + valWithIdxArr[right].val < target)
                left++;
        }
        return vector<int>();
    }
};
*/
/*
class Solution {
struct Point {
    int num;
    int idx;
};
static bool cmp(Point &a, Point &b) {
    return a.num < b.num;
}
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<Point> numIdxArr;
        for (int i = 0 ; i < nums.size(); i++) {
            numIdxArr.push_back({nums[i], i});
        }
        sort(numIdxArr.begin(), numIdxArr.end(), cmp);
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            if (numIdxArr[left].num + numIdxArr[right].num == target) {
                return {numIdxArr[left].idx, numIdxArr[right].idx};
            }
            else if (numIdxArr[left].num + numIdxArr[right].num > target)
                right -=1;
            else
                left += 1;
        }
        vector<int> ans;
        return ans;
    }/*
    unordered_map<int, int> numToIndexMap;
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (numToIndexMap.find(target-num) != numToIndexMap.end()) {
                return {i, numToIndexMap[target - num]};
            }
            numToIndexMap[num] = i;
        }
        vector<int> ans;
        return ans;
    }*/
    // };