
public class MaximumProductSubarray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	
    public int maxProduct(int[] nums) {
        int maxProduct = nums[0];
        int max = maxProduct;
        int min = maxProduct;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < 0) {
            	int temp = maxProduct;
            	max = min;
            	min = temp;
            }

            max = Math.max(nums[i], nums[i] * max);
            min = Math.min(nums[i], nums[i] * min);

            maxProduct = Math.max(maxProduct, max);
        }

        return maxProduct;
    }

}
