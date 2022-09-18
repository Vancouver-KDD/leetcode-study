public class MaximumSubarray {
	public static void main(String args[]) {
		int[] nums = {1,2,3,-10, 1,12, -12, 14};
		System.out.println(new MaximumSubarray().maxSubArray(nums));
		
		
	}
 	
    public int maxSubArray(int[] nums) {
		int maxSub = nums[0];
		int currentSum = 0;
		for (int i = 0; i < nums.length; i++) {
			if (currentSum < 0) {
				currentSum = 0;
			}
			currentSum += nums[i];
			maxSub = Math.max(maxSub, currentSum);
		}
		return maxSub;
        
    }
}
