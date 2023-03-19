// You are given an integer array coins representing coins of different denominations 
// and an integer amount representing a total amount of money.

// Return the fewest number of coins that you need to make up that amount. 
// If that amount of money cannot be made up by any combination of the coins, return -1.

// You may assume that you have an infinite number of each kind of coin.

// Input: coins = [1,2,5], amount = 11
// Output: 3
// Explanation: 11 = 5 + 5 + 1

public int coinChange(int[] coins, int amount) {
    if (amount == 0)
        return 0;
    int[] amountMap = new int[amount+1];
    Arrays.fill(amountMap, Integer.MAX_VALUE);
    amountMap[0] = 0;
    for(int i = 0; i <= amount; i++) {
        if(amountMap[i] == Integer.MAX_VALUE) continue;
        for (int coin : coins) {
            if (coin > amount - i) continue;
            amountMap[i+coin] = Math.min(amountMap[i] + 1, amountMap[i+coin]);
        }
    }
    return amountMap[amount] == Integer.MAX_VALUE ? -1 : amountMap[amount];
}
