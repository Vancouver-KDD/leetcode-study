class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto index = find(nums.begin(), nums.end(), target);
        if(index!=nums.end()) return index-nums.begin();
        else return -1;
    }
};