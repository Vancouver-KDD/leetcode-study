class Solution {
    public int maxSubArray(int[] nums) {
       int max = nums[0]; //return value
       int addingOrnot = nums[0];
       for(int i = 1; i<nums.length;i++) {
            //if nums[i] is bigger than sum of the previous nums, better to start from there
           addingOrnot = Math.max(addingOrnot + nums[i], nums[i]);
           max = Math.max(max, addingOrnot);
       }
       return max;
    }
}

//TC : O(N)