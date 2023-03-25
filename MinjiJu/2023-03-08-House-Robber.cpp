class Solution {
public:
    int rob(vector<int>& nums) {
        
        int prev2=0, prev=0, cur=0;
        
        for(auto i:nums){
            cur = max(prev, i+prev2);
            prev2 = prev;
            prev = cur;
        }
        return cur;
    }
};




/*

// space-optimized dp
class Solution {
public:
    int rob(vector<int>& A) {
        int prev2 = 0, prev = 0, cur = 0;
        for(auto i : A) {
            cur = max(prev, i + prev2);
            prev2 = prev;
            prev = cur;
        }
        return cur;
    }
}; }
};
*/