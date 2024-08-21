public class Solution {
    Dictionary<(int idx, int sum1, int sum2), int> dp;

    public bool CanPartition(int[] nums) {
        dp = new();

        return CanPartition(nums, 0, 0, 0);
    }

    public bool CanPartition(int[] nums, int idx, int sum1, int sum2) {
        if(idx >= nums.Length){
            return sum1 == sum2;
        }

        if(dp.ContainsKey((idx, sum1, sum2))){
            return dp[(idx, sum1, sum2)] == 1;
        }

        dp.Add((idx, sum1, sum2), 0);

        if(CanPartition(nums, idx+1, sum1 + nums[idx], sum2) || CanPartition(nums, idx+1, sum1, sum2 + nums[idx])){
            dp[(idx, sum1, sum2)] = 1;
            return true;
        }
        
        return false;
    }
}
