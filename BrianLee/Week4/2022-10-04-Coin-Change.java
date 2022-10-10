class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount == 0) return 0;

        Map<Integer, Integer> mem = new HashMap<>();
        getNumberOfCoins(coins, 0, amount, mem);
        return  mem.get(amount) == Integer.MAX_VALUE ? -1: mem.get(amount);
    }

    public int getNumberOfCoins(int[] coins, int level, int leftAmount, Map<Integer, Integer> mem) {
        if(leftAmount == 0) return 0;
        if(leftAmount < 0) return Integer.MAX_VALUE;

        if(mem.containsKey(leftAmount)) {
            return mem.get(leftAmount);
        }

        int min = Integer.MAX_VALUE;
        for(int coin: coins) {
            int cur = getNumberOfCoins(coins, level+1, leftAmount-coin, mem);
            if(cur != Integer.MAX_VALUE) {
                min = Math.min(min, cur + 1);
            }
        }
        mem.put(leftAmount, min);

        return min;
    }
}