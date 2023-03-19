import java.util.*;

class Solution {
    int [] memo;
    public int rob(int[] nums) {
        memo =  new int [nums.length+1];
        Arrays.fill(memo, -1);
        return rob(nums, nums.length-1);
    }
    private int rob(int [] nums, int i) {
        if(i<0) return 0;

        if(memo[i] >= 0) return memo[i];
        int result = Math.max(rob(nums, i-2)+nums[i], rob(nums, i-1));
        memo[i]= result;
        return result;
    }
}
//TC : O(N)

//참고 https://leetcode.com/problems/house-robber/solutions/156523/from-good-to-great-how-to-approach-most-of-dp-problems/