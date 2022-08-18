class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int buy = prices[0];
        int profit = 0;
        
        for (int i : prices) {
            if (i - buy > profit) {
                profit = i - buy;
            }
            if (i < buy) {
                buy = i;
            }
        }
        
        return profit;
    }
};