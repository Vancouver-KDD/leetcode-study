import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SearchinRotatedSortedArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

    public int search(int[] nums, int target) {
    	for (int i=0; i < nums.length; i++) {
    		if(nums[i]== target) {
    			return i;
    		}
    	}
    	return -1;
    }
}
