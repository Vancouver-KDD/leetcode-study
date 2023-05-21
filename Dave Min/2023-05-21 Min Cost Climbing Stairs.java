public class Solution {
    public int MinCostClimbingStairs(int[] cost) {

        int[] minimumCost = new int[cost.Length + 1];
        
        // Start iteration from step 2, since the minimum cost of reaching
        // step 0 and step 1 is 0
        for (int i = 2; i < minimumCost.Length; i++) {
            int takeOneStep = minimumCost[i - 1] + cost[i - 1];
            int takeTwoSteps = minimumCost[i - 2] + cost[i - 2];
            minimumCost[i] = Math.Min(takeOneStep, takeTwoSteps);
        }
        
        // The final element in minimumCost refers to the top floor
        return minimumCost[minimumCost.Length - 1];      
    }
}
  
//1 3 2 5 6 10 4
//    1 3 3  8 9 13
//TC: O(N)  
//SC: O(N)
    
