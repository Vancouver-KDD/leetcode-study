import java.util.*;
//dp way
class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int [][] dp = new int[n+1][amount+1];
        
        for(int i = 0; i<=amount ;i++) {
            //이후에 +1 을 더하기 때문에 Integer.MAX_VALUE +1 을 하면 Integer.MIN_VALUE가 된다.
            //ref.
            //https://stackoverflow.com/questions/9397475/why-integer-max-value-1-integer-min-value
            dp[0][i] = Integer.MAX_VALUE-1;
        }
        for(int i = 1;i<=n;i++) {
            dp[i][0] = 0;
        }
        for(int i = 1;i<=n;i++) {
            for(int j = 1;j<=amount;j++) {
                //coint[i-1] 이 임의의 amount보다 작을 때 계산 가능
                if(coins[i-1] <=j) {
                    dp[i][j] = Math.min(1+dp[i][j-coins[i-1]], dp[i-1][j]);
                }else if(coins[i-1]> j) {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        if(dp[n][amount] == Integer.MAX_VALUE-1) {
            return -1;
        }
        return dp[n][amount];
    }

//bfs
public int coinChange2(int[] coins, int amount){
    if(coins == null || coins.length == 0 || amount < 1) return 0;

    Deque<Integer> queue = new ArrayDeque<Integer>();
    Set<Integer> visited = new HashSet<Integer>();
    queue.addFirst(amount);
    visited.add(amount);
    int level = 0;

    while(!queue.isEmpty()){
      int size = queue.size();

      while(size-- > 0){
        int curr = queue.removeLast();
        if(curr == 0) return level;

        if(curr < 0) continue;

        for(int coin : coins){
          int next = curr - coin;
          if(next >= 0 && !visited.contains(next)){
            queue.addFirst(next);
            visited.add(next);
          }
        }
      }

      level++;
    }

    return -1;
  }
}
//https://leetcode.com/problems/coin-change/solutions/198007/java-bfs-solution/