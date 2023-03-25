class Solution {
public:
    int robval(vector<int>& nums){
        int a=0, b=0, res=0;
        
        for(int i=0; i<nums.size(); i++){
            res = max(nums[i]+b, a);
            b = a;
            a = res;
        }
        return res;
    }
    
    int rob(vector<int>& nums) {
        
        if(nums.size()<1) return 0;
        if(nums.size()==1) return nums[0];
        
        vector<int> v1(nums.begin()+1, nums.end()); // exclude first house
        vector<int> v2(nums.begin(), nums.end()-1); // exclude last house
        
        return max(robval(v1),robval(v2));
    }
};


/*
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size(); 
        if (n < 2) return n ? nums[0] : 0;
        return max(robber(nums, 0, n - 2), robber(nums, 1, n - 1));
    }
private:
    int robber(vector<int>& nums, int l, int r) {
        int pre = 0, cur = 0;
        for (int i = l; i <= r; i++) {
            int temp = max(pre + nums[i], cur);
            pre = cur;
            cur = temp;
        }
        return cur;
    }
};
*/