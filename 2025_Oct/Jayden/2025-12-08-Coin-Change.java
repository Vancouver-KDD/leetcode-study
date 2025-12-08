class Solution {
    /**
        Time Complexity: O(coin.length * amount)
        Space Complexity: O(amount)
     */
    public int coinChange(int[] coins, int amount) {

        // dp[i] = minimum coins needed to make amount = i
        int[] dp = new int[amount + 1];

        // must make all value of indecies other than 0 greater than amount since we're storing the min amount of coins needed to make each index
        Arrays.fill(dp, amount + 1);

        // 0 coins are needed to make amount 0
        dp[0] = 0;

        /*
        coins = [1,2,5]

        $0:0
        $1:1
        $2:1
        $3:2
        $4:2
        $5:1
        $6:2
        $7:2
        $8:3
        $9:3
        $10:2
        $11:3
         */


        for (int coin : coins) {
            for (int i = coin; i < dp.length; i++) {
                // Option 1: don't use this coin -> dp[i] stays same
                // Option 2: use this coin -> 1 + coins needed for (i - coin)
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }

        if (dp[amount] > amount)
            return -1;

        return dp[amount];
    }
}