//used a nested loop :(
class Solution {
    public int maxProduct(int[] nums) {
        int max = 0;
        if(nums.length == 1) return nums[0];
        for(int i = 0; i<nums.length-1; i++) {
            int prev = nums[i];
            for(int j = i+1; j<nums.length; j++) {
                prev = prev*nums[j];
                if(prev>max) max = prev;
                if(nums[j]>max) max = nums[j];
            }
            if(nums[i]>max) max=nums[i];
        }
        return max;
    }
}
