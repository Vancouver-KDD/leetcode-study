class Solution {
public:
    int missingNumber(vector<int>& nums) {
        map<int, int> table;
        for (int i : nums) {
            table[i] = 1;
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if (table[i] != 1) {
                return i;
            }
        }
        
        return nums.size();
    }
};