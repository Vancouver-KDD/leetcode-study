// time limit exceeded
class Solution {
public:
    int climbStairs(int n) {
        // number of methods depicts fibonacci
        // {1,2,3,5,8,13,...}
        if(n<0) return 0;
        if(n==0 || n==1) return 1;
        return climbStairs(n-1)+climbStairs(n-2);
    }
};