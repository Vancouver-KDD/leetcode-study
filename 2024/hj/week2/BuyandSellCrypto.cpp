class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int l = 0, r = 0;
        int mp = 0;

        while (r < n) {
            if (prices[r] > prices[l])
                mp = max(mp, prices[r] - prices[l]);
            else
                l = r;
            r++;
        }

        return mp;
    }
};
