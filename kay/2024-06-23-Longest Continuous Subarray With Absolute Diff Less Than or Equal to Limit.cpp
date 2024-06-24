#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

class Solution {
private:
    struct Point {
        int idx;
        int val;
        bool operator<(Point const& input) const {
            return this->val < input.val;
        }
    };
    struct Point2 {
        int idx;
        int val;
        bool operator<(Point2 const& input) const {
            return this->val > input.val;
        }
    };
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int left = 0, right = 1;
        int maxLength = 1;
        int curMax, curMin;
        priority_queue<Point> maxNumWithIdxPQ;
        priority_queue<Point2> minNumWithIdxPQ;
        maxNumWithIdxPQ.push({ left, nums[left] });
        minNumWithIdxPQ.push({ left, nums[left] });
        while (right < nums.size()) {
            maxNumWithIdxPQ.push({ right, nums[right] });
            minNumWithIdxPQ.push({ right, nums[right] });
            while (maxNumWithIdxPQ.top().idx < left)
                maxNumWithIdxPQ.pop();
            while (minNumWithIdxPQ.top().idx < left)
                minNumWithIdxPQ.pop();
            curMax = maxNumWithIdxPQ.top().val;
            curMin = minNumWithIdxPQ.top().val;
            if (abs(curMax - curMin) <= limit) {
                maxLength = max(maxLength, right - left + 1);
                right++;
            }
            else
                left++;
            if (left == right)
                right++;
        }
        return maxLength;
    }
};