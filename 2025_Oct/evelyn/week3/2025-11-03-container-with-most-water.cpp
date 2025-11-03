class Solution {
public:
    int maxArea(vector<int>& height) {
        int ans = INT_MIN;
        int left = 0;
        int right = height.size() - 1;

        while (right >left) {
            ans = max(ans, (right-left) * min(height[left], height[right]));

            if (height[right] > height[left]) left++;
            else right--;
        }

        return ans;
    }
};