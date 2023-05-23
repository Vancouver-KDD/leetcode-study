class Solution{
    public int minCostClimbingStairs(int[] cost){
        int[] res = new int[cost.length +1];
        res[cost.length] = 0;
        res[cost.length -1] = cost[cost.length-1];
        for(int i = cost.length -2; i >= 0;i--){
            res[i] = (rest[i+1] < res[i+2]) 
                ? res[i+1]+cost[i]
                : rest[i +2]+cost[i];
        }
        return Math.min(rest[0],rest[1]);
    }
}