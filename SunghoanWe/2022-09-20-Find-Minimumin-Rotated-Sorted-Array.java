import java.sql.Array;
import java.util.Arrays;

public class FindMinimuminRotatedSortedArray {
 
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

//    public int findMin(int[] nums) {
//    	Arrays.parallelSort(nums);
//        return nums[0];
//    }
	
    public int findMin(int[] nums) {
        int left = 0; 
        int right = nums.length - 1;
        while (left < right) {
            if (nums[left] < nums[right]) {
                return nums[left];
            }
            int mid = (left + right) / 2;
            if (nums[left] <= nums[mid]) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        return nums[left];
    }
}
