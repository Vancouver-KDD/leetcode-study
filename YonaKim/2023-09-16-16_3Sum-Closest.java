class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if(nums.length == 3) {
            return nums[0] + nums[1] + nums[2];
        }

        Arrays.sort(nums);
        //TODO solution
        return nums[1] + nums[2] + nums[3];
    }
}