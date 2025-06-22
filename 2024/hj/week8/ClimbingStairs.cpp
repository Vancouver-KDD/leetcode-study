class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        if (n == 2) return 2;

        vector<int> v(n + 1);
        v[1] = 1;
        v[2] = 2;

        for (int i = 3; i <= n; i++) {
            v[i] = v[i - 2] + v[i - 1];
        }

        return v[n];
    }
};
