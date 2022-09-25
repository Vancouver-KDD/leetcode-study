
public class MaximumProductSubarray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	
    public int maxProduct(int[] nums) {
        int result = nums[0];
        int imax = result;
        int imin = result;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < 0) {
            	int temp = imax;
            	imax = imin;
            	imin = temp;
            }

            imax = Math.max(nums[i], nums[i] * imax);
            imin = Math.min(nums[i], nums[i] * imin);

            result = Math.max(result, imax);
        }

        return result;
    }

}
