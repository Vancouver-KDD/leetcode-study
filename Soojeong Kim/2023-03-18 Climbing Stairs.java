class Solution {
    public int climbStairs(int n) {
        if(n==1) return 1;
        if(n==2) return 2;

        int n2 = 1, n1 = 2, result = 0;

        for(int i = 2;i<n;i++) {
            result = n2 + n1;
            n2 = n1;
            n1 = result;
        }
        return result; 
    }
}