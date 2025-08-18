class ClimbingStairs {
    public int climbStairs(int n) {
        if (n < 2) return n;

        int first = 1;
        int second = 1;
        int cur = 0;
        for (int i = 2; i <= n; i++) {
            cur = first + second;
            first = second;
            second = cur;
        }
        
        return cur;
    }
}