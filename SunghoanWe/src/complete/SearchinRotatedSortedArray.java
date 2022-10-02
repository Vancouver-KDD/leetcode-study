package complete;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SearchinRotatedSortedArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

//    public int search(int[] nums, int target) {
//    	for (int i=0; i < nums.length; i++) {
//    		if(nums[i]== target) {
//    			return i;
//    		}
//    	}
//    	return -1;
//    }
    
    public int search(int[] nums, int target) {    
	    int left = 0;
	    int right = nums.length - 1;
	    int start = 0;
	    while (left < right) {
	        if (nums[left] < nums[right]) {
	            start = left;
	            break;
	        }
	        int mid = (left + right) / 2;
	        if (nums[left] <= nums[mid]) {
	            left = mid + 1;
	        }
	        else {
	            right = mid;
	        }
	    }
	    start = left;
	
	    left = 0;
	    right = nums.length - 1;
	    if (nums[start] <= target && nums[right] >= target) {
	        left = start;
	    }
	    else {
	        right = start - 1;
	    }
	
	    while (left <= right) {
	        int mid = (left + right) / 2;
	        if (target == nums[mid]) {
	            return mid;
	        }
	
	        if (target < nums[mid]) {
	            right = mid - 1;
	        }
	        else {
	            left = mid + 1;
	        }
	    }
	
	    return -1;    
    }
}
