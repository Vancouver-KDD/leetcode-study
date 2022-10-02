package complete;
import java.util.HashMap;
import java.util.Map;

public class ProductofArrayExceptSelf {
	public static void main(String args[]) {
		int[] nums = {1,2,3,4};
		int [] result = new ProductofArrayExceptSelf().productExceptSelf(nums);
		for (int i=0; i < result.length; i++) {
			System.out.println(result[i]);
		}

	}
	
    public int[] productExceptSelf(int[] nums) {
		int[] answers = new int[nums.length];

		int prefix = 1;
		for (int i=0; i < nums.length; i++) {
			answers[i] = prefix;
			prefix *= nums[i];
		}
		int postfix = 1;
		for (int i=nums.length-1; i>=0; i--) {
			answers[i] *= postfix;
			postfix *= nums[i];
		}
		return answers;
    }
}
