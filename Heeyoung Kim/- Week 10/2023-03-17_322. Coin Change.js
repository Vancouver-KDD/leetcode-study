var coinChange = (coins, amount) => {
    if(amount === 0) return 0;
    if(amount < 0) return -1;

    let dp = new Array(amount+1).fill(Infinity);

    dp[0] = 0;

    for(let i=0; i<=amount; i++) {
        for(let j=0; j<coins.length; j++){
            if(i>=coins[j]) {
                dp[i] = Math.min(dp[i], dp[i-coins[j]] + 1);
            }
        }
    }

    const ans = dp[dp.length-1];
    return ans === Infinity? -1: ans;
}