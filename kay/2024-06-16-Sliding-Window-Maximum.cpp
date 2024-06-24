#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

class Solution {
private:
    struct Point {
        int val;
        int idx;
        bool operator<(const Point& a) const {
            return this->val < a.val;
        }
    };
    struct cmp {
        bool operator()(Point& a, Point& b) {
            return a.val < b.val;
        }
    };
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<Point> pq;
        // priority_queue<Point, vector<Point>, cmp> pq;   
        int left = 0, right = 0;
        vector<int> maxValueList;
        while (right < k && right < nums.size()) {
            pq.push({ nums[right], right++ });
            // printf("%d\n", right);
        }
        maxValueList.push_back(pq.top().val);
        while (right < nums.size()) {
            // printf("%d\n", right);
            pq.push({ nums[right], right++ });
            ++left;
            while (pq.top().idx < left)
                pq.pop();
            maxValueList.push_back(pq.top().val);
        }
        return maxValueList;
    }
};