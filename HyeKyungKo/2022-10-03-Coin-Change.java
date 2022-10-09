//Limitation: if coins is null or size is zero, return -1;
//Input: coins = [1,2,5], amount = 11 --> Output: 3
//Input: coins = [2], amount = 3  ---> Output: -1
//Input: coins = [2], amount = 1  ---> Output: -1
//Input: coins = [186,419,83,408], amount = 6249 ---> Output: 20
//Input: coins = [470,35,120,81,121], amount = 9825 ---> Output:30


//2022.10.03
//recursive 안쓴경우 
//Time complexty:O(size of coins array * amount), Space complexity: O(amount)
class Solution{
    public int coinChange(int[] coins, int amount){
        if(coins == null || coins.length == 0 || amount < 0){
            return -1;
        }
        
        if(amount == 0){
            return 0;
        }
        
        int[] minCoinChange = new int[amount+1]; 
        
        for(int i = 1; i <= amount; i++){
            
            int min = amount+1;
            for(int j = 0; j < coins.length; j++){
                int prev = i - coins[j];
                if( prev >= 0){
                    min = Math.min(min, minCoinChange[prev] +1);
                }
            }
            
            minCoinChange[i] = min;
        }
        
        
        if(minCoinChange[amount] == (amount+1)){
            //There is no coin set 
            return -1;
        }
        
        //return the minimum number of Coin set 
        return minCoinChange[amount];
    }
}



//2022.10.03
//Time Complexity: O(size of coin* amount) : coin 이 1 인 경우 (amount -coin) depth 가 amount 와 동일
//Space Complexity: O(amount) //(amount+1) is memoization table size , recursive depth 도 동일하게 최대 amount 이니까 
//                             2*amount 인것 같은데 결국 그래서 amount 인 것일까?
/*
class Solution{
    public int coinChange(int[] coins, int amount){
        if(coins == null || coins.length == 0 || amount < 0){
            return -1;
        }
        
        if(amount == 0){
            return 0;
        }
        
        //This array memorizes the minimum number of coins to make the amount of index.
        int[] numMinCoinChange = new int[amount +1]; // default value => all set '0'
        
        return findMinCoinChange(coins, amount, numMinCoinChange);
    }
    
    private int findMinCoinChange(int[] coins, int amount, int[] numMinCoinChange){
        
        if(amount < 0){
            //cannot find right coin
            return -1;
        }
        
        if(amount == 0){
            //no more coin needed.
            return 0;
        }
        
        //return the memorized result
        if(numMinCoinChange[amount] != 0){
            return numMinCoinChange[amount];
        }
        
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < coins.length; i++){
            int result = findMinCoinChange(coins, amount - coins[i], numMinCoinChange);
            if(result >=0){
                min = Math.min(min, result+1);
            }
            //System.out.println("amount:" + amount + ",coins:"+coins[i]+",resultNum:" + result +", min:"+ min);
        }
        
        if(min == Integer.MAX_VALUE){
            //no matched coins' set
            numMinCoinChange[amount] = -1;
        }else{
            //succeed to find coins' set to make the amount
            numMinCoinChange[amount] = min;
        }
        
        return numMinCoinChange[amount];
    }
}
*/