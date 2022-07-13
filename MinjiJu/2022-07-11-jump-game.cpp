// greedy approach
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int dist = 0;
        for(int i=0; i<nums.size(); i++){
            if(dist<i) return false;
            dist = max(i+nums[i],dist);
        }
        return true;
    }
};
